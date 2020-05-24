from P1.Seq1 import Seq
from P2.Client0 import Client

PRACTICE = 2
EXERCISE = 5
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

FOLDER = "../Session-04/"
FILENAME = "U5"
# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 63342

c = Client(IP, PORT)
print(c)

s = Seq()
s.read_fasta(FOLDER+FILENAME)

c.debug_talk(f"Sending {FILENAME} Gene to the server")
c.debug_talk(str(s))

