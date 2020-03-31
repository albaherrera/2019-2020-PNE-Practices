from seq0 import*

folder = "../Session-04/"
filename = "U5"
print("-----| Exercise 6 |------")
print("Gene",filename)
seq = seq_read_fasta(folder+filename)
print("frag",(seq[:20]))
print("rev",seq_reverse(seq[:20]))