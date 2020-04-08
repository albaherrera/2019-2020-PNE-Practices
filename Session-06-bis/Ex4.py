import termcolor
class Seq:

    def __init__(self, strbases):
        self.strbases = strbases
        print ("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


def generate_seqs(pattern,number):
    list = []
    for n in range (1,number+1):
        list.append(Seq(pattern * n))
    return list

def print_seqs(seqs,colors):
    for seq in seqs:
        termcolor.cprint(f"Sequence {seqs.index(seq)}: (Length: {seq.len()}) {seq}", colors)

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:","blue")
print_seqs(seq_list1,"blue")

print()
termcolor.cprint("List 2:","green")
print_seqs(seq_list2,"green")