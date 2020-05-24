from P1.Seq1 import Seq
from P2.Client0 import Client

PRACTICE = 2
EXERCISE = 7
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

FOLDER = "../Session-04/"
FILENAME = "FRAT1"
# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 58788

c1 = Client(IP, PORT)
c2 = Client(IP, PORT + 1)

print(c1)
print(c2)

s = Seq()
s.read_fasta(FOLDER + FILENAME)
bases = str(s)

length = 10

print(f"Gene {FILENAME}: {bases}")

c1.talk(f"Sending {FILENAME} Gene to the server, in fragments of {length} bases...")
c2.talk(f"Sending {FILENAME} Gene to the server, in fragments of {length} bases...")

for index in range(0,10):
    fragment = bases[index * length:(index + 1) * length]
    print(f"Fragment {index + 1}: {fragment}")

    if index % 2:
        c2.talk(f"Fragment {index + 1}: {fragment}")
    else:
        c1.talk(f"Fragment {index + 1}: {fragment}")
