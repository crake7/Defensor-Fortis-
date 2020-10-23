#!/usr/bin/env python

import scapy.all as scapy
import argparse

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    targets_list=[]
    for e in answered_list:
        targets_dict = {"IP": e[1].psrc, "MAC": e[1].hwsrc}
        targets_list.append(targets_dict)
        # print(e[1].psrc + "\t\t" + e[1].hwsrc)
        # print("---------------------------------------------")
    return targets_list

def print_result(results_list):
    print("IP\t\t\tMAC address\n---------------------------------------------")
    for target in results_list:
        print(target['IP'] + "\t\t" + target['MAC'])

def parsero():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="ip_range", help="Provide IP range & subnet mask")
    args = parser.parse_args()
    return args

args = parsero()
scan_result = scan(args.ip_range)
print_result(scan_result)

