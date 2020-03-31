from Seq1 import Seq
print("-----|Practice 1 , Exercise 8 |------")

s0 = Seq()
s1 = Seq ("ACGTGA")
s2 = Seq ("AGSTGC")

print (f"Sequence 0: (Length {s0.len()} ){s0} ")
print (f" Bases : {s0.count()}")
print (f"Rev: {s0.reverse()}")
print (f" Comp :{s0.complement()}")

print (f"Sequence 0: (Length {s1.len()} ){s1} ")
print (f" Bases : {s1.count()}")
print (f"Rev: {s1.reverse()}")
print (f" Comp :{s1.complement()}")

print (f"Sequence 0: (Length {s2.len()} ){s2} ")
print (f" Bases : {s2.count()}")
print (f"Rev: {s2.reverse()}")
print (f" Comp :{s2.complement()}")


