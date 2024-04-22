#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
#title           : sweetvenom honeypot
#description     : Program created to simulate honeypots 
#version         :0.1
#usage           :
#notes           : 
#python_version  :3.8


import os
import socket
import sys
import time
import threading
import requests

# Default ports and responses
default_ports_and_responses = {
    #User what is the most common response for windows ports
      20: "",
      21: "220 FTP Server (Version 5.4) Ready",
      53: ";; ANSWER SECTION: \n example.com.        3600    IN      A       192.168.1.1",
      80: "HTTP/1.1 200 OK \n Content-Type: text/html \n Content-Length: 1234",
      123: "this is the ntp port",
      179: "Marker: FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF \n Length: 29 \n Type: Open \n Version: 4 \n ASN: 65500 \n Hold Time: 180 \n BGP Identifier: 192.0.2.1 \n Optional Parameters Length: 0",
      443: "",
      500: "",
      587: "",
      3389: ""
}

# User-defined ports and responses
user_ports_and_responses = {}

interface = ""
max_results = 200

def print_ascii_art():
    ascii_art = """
  ********                              **   **      **                                      
 **//////                              /**  /**     /**                                      
/**        ***     **  *****   *****  ******/**     /**  *****  *******   ******  ********** 
/*********//**  * /** **///** **///**///**/ //**    **  **///**//**///** **////**//**//**//**
////////** /** ***/**/*******/*******  /**   //**  **  /******* /**  /**/**   /** /** /** /**
       /** /****/****/**//// /**////   /**    //****   /**////  /**  /**/**   /** /** /** /**
 ********  ***/ ///**//******//******  //**    //**    //****** ***  /**//******  *** /** /**
////////  ///    ///  //////  //////    //      //      ////// ///   //  //////  ///  //  // 

COMMON COMMANDS
[+] telnet <host ip> <portNumber> <enter>
    """

    print(ascii_art)

# Call print the ASCII art
print_ascii_art()

def bind(p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((interface, int(p)))
    print("Listening on Port: " + str(p))
    while True:
        s.listen(5)
        conn, addr = s.accept()
        info = (time.ctime() + " | connection from: | " + addr[0] + " on port: " + str(p))
        s.settimeout(3)  # Set a timeout value of 10 seconds (adjust as needed)
        print(info)

        with open("honeypot.log", "a") as f:
            f.write(info + "\n")

        # Send the corresponding response for the connected port
        if p in user_ports_and_responses:
            response = user_ports_and_responses[p]
        else:
            response = default_ports_and_responses.get(p, "No response defined for this port")

        print("Response for port", p)
        print(response)
        print("Response received from port {}: {}".format(p, response))
        conn.sendall(response.encode())
        conn.close()
def close():
    time.sleep(5)
    while True:
        ifex = input("To close type e(x)it: ")
        if ifex == "x" or ifex == "X":
            os._exit(1)

# User input for selecting default option
while True:
    option = input("Select an option for default ports and responses ((W)indows or (L)inux): ")
    if option == "W" or option == "w":
        break
    elif option == "L" or option == "l":
        default_ports_and_responses = {
            20: "",
            21: "220 FTP Server (Version X.X) Ready",           
            22: "SSH-2.0-OpenSSH_X.X",
            23: "Welcome to the Telnet server!", #telnet
            25: "220 example.com ESMTP Postfix", #SMTP
            53: ";; ANSWER SECTION: \n example.com.     3600    IN    A    192.0.2.123",
            67: "Offer: IP address: 192.168.0.100, Subnet mask: 255.255.255.0, Gateway: 192.168.0.1, DNS server: 8.8.8.8",
            68: "Client request: MAC address: 00:11:22:33:44:55",
            80: "HTTP/1.1 200 OK \n Server: Apache/2.4.29 (Unix) OpenSSL/1.1.1g \n Content-Type: text/html; charset=utf-8 \n Content-Length: 1234",
            110: "+OK POP3 server ready <hostname>" # pop3
        }
        break
    else:
        print("Invalid option. Please select W or L.")

# User input ports and responses
while True:
    port = input("Enter a port (or press Enter to finish): ")
    if not port:
        break
    response = input("Enter the response for port {}: ".format(port))
    user_ports_and_responses[int(port)] = response

# Merge user-defined ports and responses with defaults
ports_and_responses = {**default_ports_and_responses, **user_ports_and_responses}

jobs = []
num_results = 0
for p in ports_and_responses:
    t = threading.Thread(target=bind, args=(p,))
    jobs.append(t)
    t.start()
    num_results += 1
    if num_results >= max_results:
        break

print("Honeypot running. Press Ctrl+C to exit gracefully.")
close()
