from P2.Client0 import Client

SEQ = "ACTAGATC"
FILENAMES = ["U5","FRAT1","ADA","FXN","RNU6_269P"]

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# IP and PORT
IP = "127.0.0.1"
PORT = 53223
c = Client(IP, PORT)
print(c)

#PING
print("Testing PING...")
print(c.talk("PING"))


#GET
print("Testing GET...")
print(c.talk("GET 0"))
print(c.talk("GET 1"))
print(c.talk("GET 2"))
print(c.talk("GET 3"))
print(c.talk("GET 4"))


#INFO
print("Testing INFO...")
print(c.talk(f"INFO {SEQ}"))

#COMP
print("Testing COMP...")
print(c.talk(f"COMP {SEQ}"))

#REV
print("Testing REV...")
print(c.talk(f"REV {SEQ}"))

#GENE
print("Testing GENE...")
for FILENAME in FILENAMES:
    print(f"GENE", FILENAME)
    print(c.talk(f"GENE {FILENAME}"))