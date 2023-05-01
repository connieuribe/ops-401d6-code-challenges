#!/usr/bin/python3
from scapy.all import *

# Script: Ops 401 Class 11 Ops Challenge Solution
# Author: Alexander White edited and completed by Connie Uribe Chavez
# Date of lates revision: 01 May 2023
# Purpose: Network Security Tool with Scapy Part 1 of 3
# Purpose: TCP Port Range Scanner that tests whether a TCP port is open or closed. 
# Reference: ChatGPT
# Reference: https://subscription.packtpub.com/book/networking-&-servers/9781784399771/8/ch08lvl1sec46/sending-and-receiving-packets-with-scapy
# Reference: https://scapy.readthedocs.io/en/latest/usage.html
# ------------------------------- 

# Define host IP
host = "scanme.nmap.org"
# Define port range or specific set of ports to scan
port_range = [22, 23, 80, 443, 3389]
# Test each port in the specified range using a for loop
for dst_port in port_range:
    src_port = 1025
    response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port,flags="S"), timeout=1, verbose=0)
    #print(response.summary) # a little info
    #print(response.show()) # A LOT OF INFO
    # If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
    # Below code is from ChatGPT, edited by Connie Uribe Chavez
    if(response is not None and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12):
        print(f"Port {dst_port} is open!") # PORT IS OPEN!!
        rst_pkt = IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="R")
        send(rst_pkt, verbose=0)
    # If flag 0x14 received, notify user the port is closed.
    elif (response is not None and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14):
        print(f"Port {dst_port} is closed.")
    # If no flag is received, notify the user the port is filtered and silently dropped.
    else:
        print(f"Port {dst_port} is filtered and silently dropped.")