from pathlib import Path

def seq_ping():
    print("OK!")

def seq_read_fasta(filename):
    file_contents = Path(filename).read_text().split("\n")[1:]
    body = "".join(file_contents)
    return body

def seq_len (filename):
    return len(filename)

def seq_count_base(seq,base):
    return seq.count(base)

def seq_count(seq):
    d = {'A': seq_count_base(seq, 'A'), 'T': seq_count_base(seq, 'T'),
           'C': seq_count_base(seq, 'C'), 'G': seq_count_base(seq, 'G')}
    return d

def seq_reverse(seq):
    return seq[::-1]

def seq_complement(seq):
    all_bases = ["A","C","G","T"]
    complement = ["T","G","C","A"]
    dictionary = dict(zip(all_bases, complement))
    complement_seq = ""
    for bases in seq:
         for base, comp in dictionary.items():
                if bases == base:
                    complement_seq += comp
    return complement_seq

