#!/usr/bin/python3
import socket
import subprocess
import os, sys, socket, time, telnetlib, signal, subprocess
# Script: Ops 401 Class 36 Ops Challenge Solution
# Author: ChatGPT edited by Connie Uribe Chavez
# Date of latest revision: 06 Jun 2023
# Purpose: utilizes multiple banner grabbing approaches against a single target.
############################################################
# Performs banner grabbing using netcat against the target address at the target port; prints the results to the screen then moves on to the step below.
# Performs banner grabbing using telnet against the target address at the target port; prints the results to the screen then moves on to the step below.
# Performs banner grabbing using Nmap against the target address of all well-known ports; prints the results to the screen.
############################################################

def netcat(addr, port):
  #creatting a socket and a connection
  socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
        socket1.connect((addr, port))
  except ConnectionRefusedError:
        print("Connection refused.")
        return
  
  print("Netcat...")

  #sneding the netcat command
  command = f"nc {addr} {port}"
  print(command)
  socket1.sendall(command.encode())
  time.sleep(.5)
  socket1.shutdown(socket.SHUT_WR)

  # Repsonse placeholder
  output = ""

  # Convert the data that we received
  while True:
    data = socket1.recv(1024)
    if(not data):
      break
    output += data.decode()

  print(output)
  #close the connection
  socket1.close()


def telnet(addr, port):
    print("Telnet...")
    try:
        tn = telnetlib.Telnet(addr, port, timeout=5)
        tn.read_until(b"\n")
        output = tn.read_all().decode('utf-8')
        print(output)
        tn.close()
    except ConnectionRefusedError:
        print("Connection refused.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def nmap(addr, port):
    print("Nmap...")
    command = f"nmap -p- -sV {addr}"
    output = subprocess.check_output(command, shell=True, universal_newlines=True)
    print(output)

### MAIN ###
def main():
    # Prompt the user to enter the target address and port
    addr = input("Enter the URL or IP address: ")
    port = int(input("Enter the port number: "))

    # Perform banner grabbing using netcat
    netcat(addr, port)

    # Perform banner grabbing using telnet
    telnet(addr, port)

    # Perform banner grabbing using Nmap on well-known ports
    nmap(addr)

# Make sure to only target approved URLs or web servers you own
if __name__ == "__main__":
    main()