from pathlib import Path
f = "ADA"
file_contents = Path(f).read_text()
seq_dna = file_contents
index_finish = seq_dna.find('\n')
seq_dna = seq_dna.replace('\n','')
number_bases = len(seq_dna)
print(number_bases)

