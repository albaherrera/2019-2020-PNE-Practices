import http.client
import json

import termcolor

from P1.Seq1 import Seq

# dictionary
GENES = { "FRAT1":"ENSG00000165879",
          "ADA":"ENSG00000196839",
          "FXN":"ENSG00000165060",
          "RNU6_269P":"ENSG00000212379",
          "MIR633":"ENSG00000207552",
          "TTTY4C":"ENSG00000228296",
          "RBMY2YP":"ENSG00000227633",
          "FGFR3":"ENSG00000068078",
          "KDR":"ENSG00000128052",
          "ANK2":"ENSG00000145362"}

all_bases = ["A","C","G","T"]
# This will be used to obtain the most frequent base
counter = 0
frequent_base = ""

# Ask for a gene
gene_input = input("Write the gene name: ")

# We need to add the Id of our gene
Server = "rest.ensembl.org"
Endpoint = "/sequence/id/"
Id = GENES[gene_input]
Parameters = "?content-type=application/json"
URL = Server + Endpoint + Id + Parameters


print()
print(f"Server: {Server}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(Server)
# -- Send the request message, using the GET method.
try:
    conn.request("GET", Endpoint + Id + Parameters)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
response = json.loads(data1)

# Information of the gene
Description = response["desc"]



termcolor.cprint(f"Gene:","green",end=" ")
print(gene_input)
termcolor.cprint(f"Description:","green",end=" ")
print(Description)

# Introduce the sequence
s = Seq(response["seq"])
s_length = s.len()
termcolor.cprint(f"Total length: ", "green", end="")
print(s_length)
for b in all_bases:
    count_b = s.count_base(b)
    p = round(count_b * (100 / s_length), 1)  # percentage calculation with just 1 decimal
    termcolor.cprint(f"{b}", "blue", end=" ")
    print(f"{count_b} {p} %")

dict = s.count()  # method from P1 to find the most repeated base
list_dict = list(dict.values())
maximum = max(list_dict)
freq_base = all_bases[list_dict.index(maximum)]
termcolor.cprint("Most frequent base : ", "green", end="")
print(freq_base)

