from P2.Client0 import Client

# PORT and IP
PORT = 40974
IP = "127.0.0.1"

for index in range(0,5):
    c = Client(IP, PORT)
    c.debug_talk(f" Message : {index}")

