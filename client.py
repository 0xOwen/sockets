#!/usr/bin/env python3

import socket
import sys

HOST = '127.0.0.1'
PORT = 56000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        print('Start a conversation:')
        data1 = input()
        if data1:
            s.send(data1.encode())
        else:
            break
        data = s.recv(1024)
        if data :
            print('\033[1;32;40m Server Said: ' + repr(data.decode()) + '\033[0m' , end='\n\n')
        else:
            break

       
    s.close()
        