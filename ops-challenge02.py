#!/usr/bin/env python3
import os, time
from datetime import datetime
# Script: Ops 401 Class 02 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of lates revision: 18 Apr 2023
# Purpose: an uptime sensor tool that checks systems are responding. 
# Reference: 
# -------------------------------

#main



def check_ping(a):
    # Transmit a single ICMP (ping) packet to a specific IP every two seconds.
    respond = os.system("ping -c 1 " + a)
    time.sleep(2)
    # Evaluate the response as either success or failure.
    # Assign success or failure to a status variable.
    if respond == 0:
        ping_status = "network is active"
    else:
        ping_status = "network is down"
    return ping_status

# For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
# Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8
while True:
    ip_a = input("Enter an IP address: ")
    status = check_ping(ip_a)
    currenttime = datetime.now()
    print(currenttime, status, " to ", ip_a)






#end
