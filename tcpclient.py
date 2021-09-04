#!/usr/bin/python3
#Author: Naresh Adhikari
#Date: 09/07/2021

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip=input("Enter Server's IP address:")
server_port=input("Enter Server's Port Number:")
print("\n");

client_socket.connect((server_ip, int(server_port)))
cli_mesg=''

print("Usage: Type bye to quit connection.\n");

while cli_mesg != "bye":
    cli_mesg = input("Message TO the Server>")
    if cli_mesg != "bye":
        client_socket.send(bytes(cli_mesg,"utf8"))
        data_server = client_socket.recv(4096)
        print("Message FROM the Server>",data_server.decode());
        print("\n");
client_socket.close()
~                    
