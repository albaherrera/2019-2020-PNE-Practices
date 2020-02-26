from seq0 import*
folder = "../Session-04/"
filename = "U5"

print ("DNA file:",filename)
print("The first 20 bases are:")
print(seq_read_fasta(folder+filename)[:20])