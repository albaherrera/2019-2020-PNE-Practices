from seq0 import*
folder ="../Session-04/"
filenames = ["U5","ADA","FRAT1","FXN"]
all_bases = ["A","C","G","T"]
print("-----| Exercise 8 |------")
for filename in filenames:
    seq = seq_read_fasta (folder+filename)
    dictionary = seq_count(seq)
    list_values = list(dictionary.values())
    maximum = max (list_values)
    print("Gene:",filename,"Most frequent base:", maximum)