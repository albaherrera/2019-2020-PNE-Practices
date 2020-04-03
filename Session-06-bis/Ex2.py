class Seq:


    def __init__(self, strbases):
        self.strbases = strbases
        print ("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

def print_seqs(seqs):
    for seq in seqs:
        print(f"Sequence {seqs.index(seq)}: (Length: {seq.len()}) {seq}")

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)
