#!/usr/bin/env python

import scapy.all as scapy
import argparse

"""NETWORK SCANNER: scans network and discovers the IP and MAC address of all connected clients. 
Use Terminal and add command: <target>, <ip_range>.
Uses Scapy library(tool for manipulating network packets)."""


def parsero():
    """Accepts <target>, <ip_range> and <help> on bash terminal."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="ip_range", help="Provide IP range & subnet mask")
    args = parser.parse_args()
    return args

def scan(ip):
    """Sends an ARP request + L2 packet using broadcast MAC address destination.
    Creates a list with answered packets."""
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=5, verbose=False)[0]
    targets_list=[]
    for host in answered_list:
        targets_dict = {"IP": host[1].psrc, "MAC": host[1].hwsrc}
        targets_list.append(targets_dict)
        # print(e[1].psrc + "\t\t" + e[1].hwsrc)
        # print("---------------------------------------------")
    return targets_list

def print_result(results_list):
    """Prints results in a list."""
    print("IP\t\t\tMAC address\n---------------------------------------------")
    for target in results_list:
        print(target['IP'] + "\t\t" + target['MAC'])
        

args = parsero()
scan_result = scan(args.ip_range)
print_result(scan_result)

