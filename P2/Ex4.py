from P2.Client0 import Client
PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 63342


# -- Create a client object
c = Client(IP, PORT)

print(c)

c.debug_talk("Message 1---")
c.debug_talk("Message 2: Testing !!!")