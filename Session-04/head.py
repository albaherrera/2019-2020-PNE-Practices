from pathlib import Path
f = "RNU6_269P"
with open('RNU6_269P', 'r') as f:
 header = next(f).replace("\n", "").split(",")
 print("First line of the RNU6_269P file: ", header)
