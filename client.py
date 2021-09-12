#!/usr/bin/python3
#Date: 09/10/2021
#Disclaimer: This program code is written or adapted or imported from different sources for education purpose only. 
#Usage of this code for any 
#other purpose beyond education is not permitted. 
#The author pays due credit to the source or original author(s), without explicitly taking their names.

import socket#from socket import *;

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
client.send(b'I am CLIENT')
from_server = client.recv(4096)
client.close()
print("from server ",from_server.decode());
