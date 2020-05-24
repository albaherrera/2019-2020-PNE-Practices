from P1.Seq1 import Seq

folder = "../Session-04/"
filename = "U5"

print("-----|Practice 1 , Exercise 9 |------")

s0 = Seq()

print (f"Sequence 0: (Length {s0.len()} ){s0.read_fasta(folder + filename)} ")
print (f" Bases : {s0.count()}")
print (f"Rev: {s0.reverse()}")
print (f" Comp :{s0.complement()}")

