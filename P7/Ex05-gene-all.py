import http.client
import json
from typing import List

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

# Now we have to print the information of all the genes that are in the dictionary
for G in GENES:

    # We dont have to ask the user for a gene, we print all of them
    Server = "rest.ensembl.org"
    Endpoint = "/sequence/id/"
    Id = GENES[G]
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
    print(G)
    termcolor.cprint(f"Description:","green",end=" ")
    print(Description)


    # Introduce the sequence
    s = Seq(response["seq"])
    s_length = s.len()
    counter_A = s.count_base("A")
    counter_C = s.count_base("C")
    counter_G = s.count_base("G")
    counter_T = s.count_base("T")
    per_A = "{:.1f}".format(100 * counter_A / s_length)
    per_C = "{:.1f}".format(100 * counter_C / s_length)
    per_G = "{:.1f}".format(100 * counter_G / s_length)
    per_T = "{:.1f}".format(100 * counter_T / s_length)

    # Print the length
    termcolor.cprint(f"Total length:","green",end=" ")
    print(s_length)

    termcolor.cprint(f"A","blue",end=" ")
    print(f"{counter_A} {per_A}%")
    termcolor.cprint(f"C","blue",end=" ")
    print(f"{counter_C} {per_C}%")
    termcolor.cprint(f"G","blue",end=" ")
    print(f"{counter_G} {per_G}%")
    termcolor.cprint(f"T","blue",end=" ")
    print(f"{counter_T} {per_T}%")

    # For printing the most frequent base
    c = s.count()
    ci = c.items()
    for a,b in ci:
        while b > counter:
            frequent_base = a
            counter = b
    termcolor.cprint(f"Most frequent base:","green",end=" ")
    print(frequent_base)