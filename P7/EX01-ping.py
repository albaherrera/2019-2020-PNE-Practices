import http.client
import json
import termcolor

Server = "rest.ensembl.org"
Endpoint = "info/ping"
Parameters = "?content-type=application/json"
URL = Server + Endpoint + Parameters

print()
print(f"Server: {Server}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(Server)
# -- Send the request message, using the GET method.
try:
    conn.request("GET", Endpoint + Parameters)
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

if response["ping"] == 1:
    print ("PING OK! Data base is running")





