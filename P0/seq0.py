from pathlib import Path

index=0
def seq_ping():
    print("OK!")
def seq_read_fasta(filename):
    file_contents = Path(filename).read_text().split("\n")[1:]
    body = "".join(file_contents)
    return body
def seq_len (seq: object) -> object:
    length = len(seq)
    return length
def seq_count_base(seq,base):
    counter = 0
    for c in seq:
        if c == base:
            counter =+1
    return counter
