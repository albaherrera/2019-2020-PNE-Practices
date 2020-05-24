from P1.Seq1 import Seq

s0 = Seq()
s1 = Seq ("ACTGA")
s2 = Seq ("AFCTGS")

all_bases = ["A","C","G","T"]

print("-----| Practice 1, Exercise 5 |------")

print (f" Sequence 0 : (Length  {s0.len()} ), {s0}")

for base in all_bases:
    print (base  + ":", s0.count_base (base), end=" ")

print (f" Sequence 1 : (Length  {s1.len()} ) , {s1}")

for base in all_bases:
    print (base  + ":", s1.count_base (base), end=" ")


print (f" Sequence 2 : (Length  {s2.len()} ) , {s2}")

for base in all_bases:
    print (base  + ":", s2.count_base (base), end=" ")
