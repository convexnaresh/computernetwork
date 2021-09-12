#!/usr/bin/python3
#Date: 09/10/2021
#Disclaimer: This program code is written or adapted or imported from different sources for education purpose only. 
#Usage of this code for any 
#other purpose beyond education is not permitted. 
#The author pays due credit to the source or original author(s), without explicitly taking their names.

import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#tcp protocol
serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
serv.bind(('127.0.0.1', 8080))
print("server waiting to listen connection");
serv.listen(5)
while True:
    conn, addr = serv.accept()
    print("server accepted a connection",addr);
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data.decode()
        print (from_client)
        conn.send(b'I am SERVER')
    conn.close()
    print ('client disconnected')
serv.close()
