#!/usr/bin/python3
from scapy.all import *
import ipaddress
# Script: Ops 401 Class 12 Ops Challenge Solution
# Author: ChatGPT edited, tested and completed by Connie Uribe Chavez
# Date of lates revision: 02 May 2023
# Purpose: Network Security Tool with Scapy Part 2 of 3
# Purpose: ICMP Ping Sweep 
# Reference: ChatGPT
############################################

# ICMP Ping Sweep tool function
def icmp_ping_sweep(network):
    # Initialize an IPv4Network
    ip4_network = ipaddress.IPv4Network(network)
    # Create a list of all host IP addresses in the network
    all_hosts = list(ip4_network.hosts())
    # Remove the network address and broadcast address from the list
    all_hosts.pop(0)
    all_hosts.pop(-1)
    # Counter
    online_hosts = 0

    # Ping each host and print the result
    for host in all_hosts:
        response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)

        if response is None:
            print(f"{host} is down or unresponsive.")
        elif response.haslayer(ICMP) and response.getlayer(ICMP).type == 3 and response.getlayer(ICMP).code in [1, 2, 3, 9, 10, 13]:
            print(f"{host} is actively blocking ICMP traffic.")
            online_hosts += 1
        else:
            print(f"{host} is online and responding.")
            online_hosts += 1

    print(f"Number of online hosts: {online_hosts}")

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

# User menu
while True:
    print("Select an option:")
    print("1. TCP Port Range Scanner")
    print("2. ICMP Ping Sweep")
    print("3. Quit")
    choice = input("Enter your choice (1, 2 or 3): ")
    
    if choice == "1":
        # # Define host IP
        # host = "scanme.nmap.org"
        # # Define port range or specific set of ports to scan
        # port_range = [22, 23, 80, 443, 3389]
        
        # Define host IP
        host = input("Enter host IP to scan: ")
        # Define port range or specific set of ports to scan
        port_range = input("Enter port range (e.g. 1-1024) or specific set of ports to scan (e.g. 22,80,443): ").split(",")
        if "-" in port_range[0]:
            port_range = range(int(port_range[0].split("-")[0]), int(port_range[0].split("-")[1])+1)
        else:
            port_range = [int(p) for p in port_range]
        tcp_port_range_scanner(host, port_range)
    elif choice == "2":
        # Prompt user for network address including CIDR block
        network = input("Enter the network address (e.g. 10.10.0.0/24): ")
        icmp_ping_sweep(network)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
