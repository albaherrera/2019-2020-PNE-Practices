from pathlib import Path
f = "U5"
with open('U5', 'r') as f:
    for line in f:
        read_info = f.read()
        print(read_info)