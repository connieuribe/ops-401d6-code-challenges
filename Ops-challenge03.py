#!/usr/bin/env python3
import os, time, smtplib
from datetime import datetime
from getpass import getpass
# Script: Ops 401 Class 03 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of lates revision: 20 Apr 2023
# Purpose: uptime sensor tool that checks systems are responding by adding a feature that notifies you of interesting status changes.
# Reference: 
# -------------------------------

#main
# Ask the user for an email address and password to use for sending notifications.
# Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
# Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.
# Declare variables
up = "Network is active"
down = "Network is down"
last = 0
pint_result = 0
email = input("Enter your email address: ")
password = getpass("Enter your passowrd: ")
ip = input("Provide an IP address you would like to monitor: ")

# Declare functions
# Function to handle the up alert
def send_upAlert():
    now = datetime.now()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email, password)
    message = "Your server came back to live!"
    s.sendmail("hearbeat@bot.com", email, message)
    s.quit

# Function that dows the pint test
def ping_test():
    if((pint_result != last) and (pint_result == up)):
        last = up
        send_upAlert()
    elif ((pint_result != last) and (pint_result == down)):
        send_upAlert()
        last = down
    
    response = os.system("ping -c +1 " + ip)
    if response == 0:
        ping_result = up
    else:
        ping_result = down

# infinite loop
while True:
    ping_test()
    time.sleep(2)


#end
