from P0.seq0 import*
folder = "../Session-04/"
filenames = ["U5","ADA","FRAT1","FXN"]
all_bases = ["A","C","T","G"]

print("-----| Exercise 4 |------")
for filename in filenames:
    seq = seq_read_fasta(folder+filename)
    print("Gene ",filename,":")
    for base in all_bases:
        print (base,":",seq_count_base(seq,base))
