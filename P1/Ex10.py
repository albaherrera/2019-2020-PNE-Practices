from P1.Seq1 import Seq

folder = "../Session-04/"
filenames = ["U5","ADA","FRAT1","FXN","RNU6_269P"]
all_bases = ["A","C","G","T"]

print("-----|Practice 1 , Exercise 10 |------")
for filename in filenames:
    s0 = Seq()
    s0.read_fasta(folder + filename)
    dictionary = s0.count()
    list_values = list(dictionary.values())
    maximum = max(list_values)
    print(f"Gene {filename}: Most frequent Base: {all_bases[list_values.index(maximum)]}")