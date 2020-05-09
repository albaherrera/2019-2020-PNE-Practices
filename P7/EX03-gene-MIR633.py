import http.client
import json
import termcolor

# We need to add the Id of our gene
Server = "rest.ensembl.org"
Endpoint = "/sequence/id/"
Id = "ENSG00000207552"
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
Gene = "MIR633"
Description=response["desc"]
Bases=response["seq"]

termcolor.cprint(f"Gene:","green",end=" ")
print(Gene)
termcolor.cprint(f"Description:","green",end=" ")
print(Description)
termcolor.cprint(f"Bases:","green",end=" ")
print(Bases)