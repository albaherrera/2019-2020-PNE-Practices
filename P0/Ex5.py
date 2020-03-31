from seq0 import*
folder = "../Session-04/"
filenames = ["U5","ADA","FRAT1","FXN"]
all_bases = ["A","C","G","T"]

print("-----| Exercise 5 |------")
for filename in filenames:
    seq = seq_read_fasta(folder+filename)
    print ("Gene",filename,":",seq_count(seq))
