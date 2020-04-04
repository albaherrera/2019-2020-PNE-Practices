import socket

# SERVER IP, PORT
PORT = 8080
IP = "10.0.2.15"

while True:

  # -- Ask the user for the message
    msg = input("Say something")

  # -- Create the socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

  # -- Establish the connection to the Server
    s.connect((PORT,IP))

  # -- Send the user message
    s.send(str.encode("Hello user"))

  # -- Close the socket
    s.close()