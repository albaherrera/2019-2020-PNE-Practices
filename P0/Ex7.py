from seq0 import*
all_bases = ["A","C","G","T"]
folder ="../Session-04/"
filename = "U5"
print("-----| Exercise 7 |------")
seq = (seq_read_fasta(folder+filename))
print("frag",(seq_read_fasta(folder+filename)[:20]))
print("comp",(seq_complement(seq)[:20]))

