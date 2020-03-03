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
