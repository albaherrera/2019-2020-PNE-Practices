from P1.Seq1 import Seq

print("-----|Practice 1 , Exercise 6 |------")

s0 = Seq()
s1 = Seq ("AGTGCA")
s2 = Seq ("ADCDGD")

print (f"Sequence 0 : (Length {s0.len()}) , {s0} ")
print (f" Bases : {s0.count()}")

print (f" Sequence 1 : (Length {s1.len()} ) , {s1}")
print (f" Bases : {s1.count()}")

print (f" Sequence 2 : (Length {s2.len()} ), {s2}")
print (f" Bases : {s2.count()}")