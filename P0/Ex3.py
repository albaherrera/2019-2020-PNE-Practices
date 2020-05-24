from P0.seq0 import*
folder = "../Session-04/"
filenames = ["U5","ADA","FRAT1","FXN"]
print("-----| Exercise 3 |------")
for gene_name in filenames:
    seq = seq_read_fasta(folder+gene_name)
    print("Gene",gene_name," ---> Length:",seq_len(seq))
