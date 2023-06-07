import socket
import subprocess

def netcat(addr, port):
    print("Netcat...")
    command = f"nc {addr} {port}"
    output = subprocess.check_output(command, shell=True, universal_newlines=True)
    print(output)

def telnet(addr, port):
    print("Telnet...")
    # Perform telnet banner grabbing here
    # You can use the telnetlib module to establish a connection and retrieve the banner

def nmap(addr):
    print("Nmap...")
    command = f"nmap {addr}"
    output = subprocess.check_output(command, shell=True, universal_newlines=True)
    print(output)

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
main()
