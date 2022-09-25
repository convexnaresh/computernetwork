#!/usr/bin/python3

#Author: Naresh Adhikari
#Date: 09/07/2021

#Disclaimer: This program code is written or adapted or imported from different sources for education purpose only. 
#Usage of this code for any 
#other purpose beyond education is not permitted. 
#The author pays due credit to the source or original author(s), without explicitly taking their names.


import socket

##Variables

server_ip="127.0.0.1"
server_port=8889

print("I am a server. My IP address is 127.0.0.1 and I listen to port number is 8889.")
print("My socket is [127.0.0.1 8889, TCP]")
print ("Any client can connect to me for chatting!!");

#Creating a socket interface using TCP protocol.
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
serv_socket.bind((server_ip, int(server_port)))

#Some message
print("\t(Server started! Server waiting for a connection from clients ...)");
count=0;

#Server listens to the socket..
serv_socket.listen(5)
while True:

    #Server accepts a connection.
    conn_socket, client_addr = serv_socket.accept()
    print("Info: Server accepted a connection from client ",client_addr);
    client_data = ''

    #do read data while there is data from server.
    while True:

        data = conn_socket.recv(4096)
        
        if not data: break
        client_data = data.decode()
        print("Message FROM a client> ", client_data)
        msgtokens=client_data.split(":")
        if count==0:
            conn_socket.send(bytes("Hi "+msgtokens[0]+", how are you?","utf8"))
        elif count==1:
            conn_socket.send(bytes("I am fine too.","utf8"))
        elif client_data == "bye" or client_data == "Bye":
            conn_socket.send(bytes("Bye.","utf8"))
        else:
            conn_socket.send(bytes("I cannot talk more. Bye!","utf8"))
        count=count+1

    #Close the socket.
    conn_socket.close()
    print ('Info: Connection disconnected!')
