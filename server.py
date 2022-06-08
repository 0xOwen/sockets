#!/usr/bin/env python3

import socket
import sys

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 55000        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('The connected client address is', addr)
        while True:
            print('Start a conversation')
            data1 = input()
            if data1:
                conn.send(data1.encode())
            else:
                break
            data = conn.recv(1024)
            if  data:
                print('\033[1;34;40m The client said: ' + repr(data.decode()) + '\033[0m', end='\n\n') 
            else:
                break
            
    conn.close()
