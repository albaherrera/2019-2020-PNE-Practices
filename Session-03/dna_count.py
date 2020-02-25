
counter_a = 0
counter_c = 0
counter_g = 0
counter_t = 0

print (dna_seq)
print (len(dna_seq))
for carac in dna_seq:
    if carac == 'A':
        counter_a+=1
    elif carac =='C':
        counter_c+=1
    elif carac =='G':
        counter_g+=1
    elif carac =='T':
        counter_t+=1
print("A :", counter_a)
print("C :",counter_c)
print("G :", counter_g)
print("T:", counter_t)

