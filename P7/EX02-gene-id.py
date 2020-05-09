import termcolor

print ("Dictionary of Genes!")

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

print (f"There are {len(GENES)} in the dictionary")

for g in GENES:
    termcolor.cprint(f"{g}","green", end="")
    print(f": --> {GENES[g]}")
