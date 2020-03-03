import socket
IP = "212.128.253.155"
PORT = 8080

#...Step 1: Creating the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#..Step 2: Bind the socket to the servers IP ad PORT
ls.bind((IP,PORT))

#... Step 3: convert into a listening socket
ls.listen()

print("Server is configured!")
while True:
    try:
        # ...Step 4: Wait for clients to connect
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print ("Server is done")
        ls.close()
        exit()
    else:

        # ... Step 5 :Receiving information from the client

        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()
        print(f"Received message:{msg}")

        # ...Step 6: sEnd aresponse message to the client

        response = "Hi, Im a happy server :-)"
        cs.send(response.encode())
        cs.close()




#...Step 4: Wait for clients to connect
(cs , client_ip_port) = ls.accept()

#... Step 5 :Receiving information from the client

msg_raw = cs.recv(2000)
msg = msg_raw.decode()
print (f"Received message:{msg}")

#...Step 6: sEnd aresponse message to the client

response = "Hi, Im a happy server :-)"
cs.send(response.encode())
ls.close()
