index=0
def seq_ping():
    print("OK!")
def seq_read_fasta(filename):
    file_contents = pathlib.Path(filename).read_text().split("\n")[1:]
    body = "".join(file_contents)
    return body



