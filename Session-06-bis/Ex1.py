class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        print ("New sequence created!")

    def __str__(self):
        return self.strbases

s1=Seq("DDDD")
s2=Seq("AGTCTA")

print(f" Sequence 1: {s1}")
print (f" Sequence 2: {s2}")
