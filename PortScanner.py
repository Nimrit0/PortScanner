#!/usr/bin/env python3

# created by Nirmit Baskota

# working mechanism of tool
# python3 PortScanner [Target_Ip] [Scan Upto Port]
# scan up to 1000 ports by default:

import sys
import socket
from datetime import datetime

def synerror():
    print("Syntax error!")
    print("Either missing an argument or more argument is passed")
    print("python3 PortScanner [Target_Ip] //optional part [Scan Upto Port]")

# Check if the correct number of arguments are provided
if (len(sys.argv) == 2) or (len(sys.argv) == 3):
    target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4
    scan_upto = int(sys.argv[2]) if len(sys.argv) == 3 else 1000
else:
    synerror()
    sys.exit()

# Print a banner with information on which host we are about to scan
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)
flag = 0

try:
    # Scan ports in the specified range
    for port in range(1, scan_upto + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        # Returns an error indicator
        result = s.connect_ex((target, port))
        if result == 0:
            flag = 1
            print(f"Port {port}: Open")
        s.close()

    # Print scanning stopped time
    print("Scanning Stopped at : " + str(datetime.now()))

    if flag == 0:
        print("-" * 50)
        print("None of the ports are open")
        print("Try using other ports")
        print("-" * 50)

except KeyboardInterrupt:
    print("\nExiting Program !!!!")
    sys.exit()
except socket.gaierror:
    print("\nHostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    print("\nServer not responding !!!!")
    sys.exit()
