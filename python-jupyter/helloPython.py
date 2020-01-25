#!/usr/bin/env python3

import socket
import sys

#check command line args
if (len(sys.argv) != 2):
    print ("Incorrect command line arguments. Please enter the IP address of the server (only)")
    quit()

serverIP = sys.argv[1]
serverPort = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverIP, serverPort))
msg = "Hello in Python\n"
print ("Sending: ", msg)
s.send(msg.encode());
response = s.recv(128)
print("Received: ", response.decode())
s.close()
