from pathlib import Path

class Seq:
    """A class for representing sequence objects """
    def __init__(self, strbases ="NULL"):
        if strbases == "NULL":
            self.strbases = "NULL"
            print ("NULL sequence created!")
            return
#EX1 (Session 6) --> We will prove that a wrong base will return an error.

        for base in strbases:
            all_bases = ["A","C","G","T"]
            if base not in all_bases:
                self.strbases = "Invalid sequence"
                print ("Invalid sequence")
                return
        self.strbases = strbases
        print ("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "Invalid sequence":
            return 0
        return len(self.strbases)

    def count_base(self,base):
        if self.strbases == "NULL" or self.strbases == "Invalid sequence":
            return 0
        return self.strbases.count(base)

    def count(self):
        all_bases = ["A", "C", "T", "G"]
        count_bases = []
        for base in all_bases:
            count_bases.append(self.count_base(base))
        dictionary = dict(zip(all_bases, count_bases))
        return dictionary

    def reverse(self):
        if self.strbases == "NULL" or self.strbases == "Invalid sequence":
            return self.strbases
        else:
         return self.strbases[::-1]

    def complement (self):
        if self.strbases =="NULL" or self.strbases == "Invalid sequence":
            return self.strbases
        all_bases = ["A","C","G","T"]
        complement_b = ["T","G","C","A"]
        new_seq = ""
        for base in self.strbases:
            if base == "A":
                 new_seq +="T"
            elif base == "T":
                new_seq += "A"
            elif base =="G":
                new_seq+= "C"
            elif base == "C":
                new_seq += "G"
        return new_seq


    def read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        body = file_contents.split('\n')[1:]
        self.strbases = "".join(body)
        return self






class Gene(Seq):
    pass

