#Author: Naresh Adhikari
#Date: 09/07/2021
#Note: This program is just for learning in this course. It is adapted from different online resources.

#!/usr/bin/python3
import socket
server_ip=input("Enter server's IP: ");
server_port=input("Enter server's port #: ");

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#tcp protocol
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
serv_socket.bind((server_ip, int(server_port)))

print("Server started...");
print("\tServer IP:",server_ip);
print("\tServer Port:",int(server_port))
print("\t(Server waiting for a connection from a client(s))");
print("......\n")
count=0;



serv_socket.listen(5)
while True:
    conn_socket, client_addr = serv_socket.accept()
    print("Info: Server accepted a connection from client ",client_addr);
    client_data = ''
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


    conn_socket.close()
    print ('Info: Connection disconnected!')
