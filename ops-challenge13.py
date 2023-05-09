#!/usr/bin/python3
from scapy.all import *
import ipaddress

# Script: Ops 401 Class 13 Ops Challenge Solution
# Author: ChatGPT edited, tested and completed by Connie Uribe Chavez
# Date of latest revision: 03 May 2023
# Purpose: Network Security Tool with Scapy Part 3 of 3
# Purpose: The final iteration of your network scanning tool
# Reference: ChatGPT

# ICMP Ping Sweep tool function
def icmp_ping_sweep(ip):
    # Initialize an IPv4Network
    try:
        ip4 = ipaddress.IPv4Address(ip)
    except ipaddress.AddressValueError:
        print(f"Invalid IP address: {ip}")
        return
    # Ping each host and print the result
    response = sr1(IP(dst=str(ip4))/ICMP(), timeout=1, verbose=0)
    if response is None:
        print(f"{ip4} is down or unresponsive.")
    elif response.haslayer(ICMP) and response.getlayer(ICMP).type == 3 and response.getlayer(ICMP).code in [1, 2, 3, 9, 10, 13]:
        print(f"{ip4} is actively blocking ICMP traffic.")

    else:
        print(f"{ip4} is online and responding.")
        portList = [7,20,21,22,23,25,53,69,80,88,102,110,135,137,139,143,381,383,443,464,465,587,636,691,902,989,990,993,995,1025,1194,1337,1589,1725,2082,2083,2483,2484,2967,3074,3306,3724,4664,5432,5900,6665,8000,8222]
        tcp_port_range_scanner(ip, portList)




# TCP Port Range Scanner function
def tcp_port_range_scanner(host, port_range):
    # Test each port in the specified range using a for loop
    for dst_port in port_range:
        src_port = 1025
        response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port,flags="S"), timeout=1, verbose=0)
        if response is not None and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            print(f"Port {dst_port} is open!")
            rst_pkt = IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="R")
            send(rst_pkt, verbose=0)
        elif response is not None and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
            print(f"Port {dst_port} is closed.")
        else:
            print(f"Port {dst_port} is filtered and silently dropped.")

while True:
    # Prompt user for host IP
    host = input("Enter host IP to scan: ")
    icmp_ping_sweep(host)
    # Prompt user to continue or quit
    choice = input("Scan another host? (Y/N): ")
    if choice.lower() == "y":
        continue
    else:
        break

