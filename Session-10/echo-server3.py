import termcolor
import socket
# Create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# PORT and IP
PORT = 40974
IP = "127.0.0.1"

# Link IP and PORT
ls.bind((IP, PORT))


# Listening if there are clients
ls.listen()
print(f"The server is configured!")
print(f"Waiting for Clients to connect")

# When a client is connected
ls.accept()
print(f"A client has connected to the server!")
connections = 0
client_l = []


while connections < 5:
    print(f"Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()

    #  Server stopped by the user
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # Close the listenning socket and exit
        ls.close()
        exit()

    #This will only work when there are no errors detected

    else:
        print(f"A client has connected to the server!")
        connections +=1

        # Recieve the msg (bytes)
        msg_raw = cs.recv(2048)

        # Decode the msg for reading it
        msg = msg_raw.decode()

        #Counting connections
        print(f"CONNECTION:{connections}.Client IP, PORT({IP},{PORT})")
        client_l.append(client_ip_port)

        # Print in green the msg
        print(f"Message received: ", end="")
        termcolor.cprint(msg, "green")


        # Send the msg to the client
        response = "ECHO: " + msg + "\n"

        # Encode the msg
        cs.send(response.encode())

        # Close the socket
        cs.close()

    # Counter of clients
    print("The following clients has connected to the server : ")

    for index, client in enumerate(client_l):
        print(f"Client {index}: {client}")

    ls.close()
