#!/usr/bin/env python
import scapy.all as scapy

def get_mac(ip):
    '''Create an ARP packet with provided ip.
    Create a L2 frame with MAC address used for broadcast.
    Send timed packed and only receive the answered list(out of the two lists),
    return only the element of a list of couples that contains the answer
    '''
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def sniff(interface):
    '''Sniff the interface provided and include call back function for every packet'''
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    '''Check if the sniffed packet is an ARP packet and whether contains a response
    packet (as opposed to a request).
    Get and compare the real mac from of the router vs the one sent on the ARP packet.
    '''
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        # print(packet.show())
        try:
            real_mac = get_mac(packet[scapy.ARP].psrc)
            response_mac = packet[scapy.ARP].hwsrc

            if real_mac != response_mac:
                print('Someone is trying to spoof your ARP!')

        except IndexError:
            pass

sniff('eth0')