from Client0 import Client
from P1.Seq1 import Seq

PRACTICE = 2
EXERCISE = 6
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

FOLDER = "../Session-04/"
FILENAME = "FRAT1"
# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 63342

c = Client(IP, PORT)
print(c)

s=Seq()
s.read_fasta(FOLDER+FILENAME)
bases = str(s)
length = 10

print(f"Gene {FILENAME}: {bases}")

c.talk(f"Sending {FILENAME} gene,in fragments of {length} bases")


for i in range (0,5):
    fragment = bases[i * length:(i + 1) * length]
    print(f"Fragment {i+1}: {fragment}")
    c.talk(f"Fragment {i + 1}: {fragment}")


