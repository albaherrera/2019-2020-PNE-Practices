import http.server
import json
import socketserver
from pathlib import Path

import termcolor

from P1.Seq1 import Seq

# Define the Server's port and the folder
PORT = 8080
FOLDER = "../Session-04/"

Server = "rest.ensembl.org"
Parameters = "?content-type=application/json"
counter = 0
all_bases = ["A","C","G","T"]
c = []
p = []



# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Define the type of content returned by the server
        content_type = "text/html"

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Processing the request line
        req = self.requestline.split(" ")

        # Path will be: "/"
        path = req[1]

        # We will need to split the "?" in order to leave the msg alone
        argument = path.split("?")

        # We define our first argument to determine if we could continue or an error in thrown
        arg0 = argument[0]

        contents = Path("Error.html").read_text()
        status = 404

        # All the information appears in "form-4.html"
        if arg0 == "/":
            contents = Path("index.html").read_text()
            status = 200

        elif arg0 == "/listSpecies":
            try:
                Endpoint = "/info/species"
                conn = http.client.HTTPConnection(Server)
                conn.request("GET", Endpoint + Parameters)
                r1 = conn.getresponse()
                data1 = r1.read().decode("utf-8")
                response = json.loads(data1)
                d = response["species"]
                length = len(d)
                limit = argument[1]
                l = limit.split("=")[1]
                limit_ = l.split("&msg")[0]
                counter = 0
                contents = """
                           <!DOCTYPE html>
                           <html lang = "en">
                           <head>
                           <meta charset = "utf-8" >
                             <title>Basic Level</title >
                           </head >
                           <body style="background-color:lightblue;">
                           </body>
                           </html>
                           """
                contents += f"<p>The total number of species in the ensembl is : {length} </p>"


                if len(limit[1]) in range(1, length):
                    contents += f"<p>The limit you have selected is: {limit_} </p>"
                    contents += f"<p>The name of the species are: </p>"
                    for i in d:
                        if counter < int(limit_):
                            contents += f"* {i['display_name']} "
                            contents += f"<br><br>"
                            counter += 1


                else:
                    contents = Path("Error.html").read_text()
                    status = 404



                contents += f"""<p><a href="/">Main page </a></body></html>"""
                status = 200


            except ValueError:
                contents = Path("Error.html").read_text()
                status = 404


            except KeyError:
                contents = Path("Error.html").read_text()
                status = 404



        elif arg0 == "/karyotype":
            try:
                s = argument[1]
                species = s.split("=")[1]
                Endpoint = f"/info/assembly/{species}"
                conn = http.client.HTTPConnection(Server)
                conn.request("GET", Endpoint + Parameters)
                r1 = conn.getresponse()
                data1 = r1.read().decode("utf-8")
                karyotype_response = json.loads(data1)
                k = karyotype_response["karyotype"]

                contents = """
                <!DOCTYPE html>
                <html lang = "en">
                <head>
                <meta charset = "utf-8" >
                  <title>Basic Level</title >
                </head >
                <body style="background-color:lightblue;">
                """
                contents += f"The names of the chromosomes are:"
                for j in k:
                    contents += f"<p> * {j} </p>"

                contents += f"""<p><a href="/">Main page </a></body></html>"""

                status = 200

            except ValueError:
                contents = Path("Error.html").read_text()
                status = 404
            except KeyError:
                contents = Path("Error.html").read_text()
                status = 404

        elif arg0 == "/chromosomeLength":
            try:
                Endpoint = "/info/assembly/"
                s = argument[1]
                spl = s.split("=")
                species= spl[1].split("&")
                conn = http.client.HTTPConnection(Server)
                conn.request("GET", Endpoint + species[0] + Parameters)
                r1 = conn.getresponse()
                data1 = r1.read().decode("utf-8")
                cl = json.loads(data1)
                n = cl['top_level_region']
                contents = """
                <!DOCTYPE html>
                <html lang = "en">
                <head>
                <meta charset = "utf-8" >
                  <title>Basic Level</title >
                </head >
                <body style="background-color:lightblue;">
                """

                for m in n:
                    if m['name'] == spl[-1]:
                        contents += f"<p>The length of the chromosome is: {m['length']}</p>"
                    else:
                        contents = Path("Error.html").read_text()
                        status = 404


                contents += f"""<p><a href="/">Main page </a></body></html>"""
                status = 200

            except ValueError:
                contents = Path("Error.html").read_text()
                status = 404
            except KeyError:
                contents = Path("Error.html").read_text()
                status = 404

        elif arg0 == "/geneSeq":
            try:
                s = argument[1]
                gene = s.split("=")[1]
                Endpoint = f"/xrefs/symbol/homo_sapiens/{gene}"
                conn = http.client.HTTPConnection(Server)
                conn.request("GET", Endpoint + Parameters)
                r1 = conn.getresponse()
                data1 = r1.read().decode("utf-8")
                d1 = json.loads(data1)
                d = d1[0]
                idd = d["id"]
                Endpoint_ = f"sequence/id/{idd}"
                conn = http.client.HTTPConnection(Server)
                conn.request("GET", Endpoint_ + Parameters)
                r2 = conn.getresponse()
                d2 = r2.read().decode("utf-8")
                d_ = json.loads(d2)
                s = d_["seq"]
                contents = """
                <!DOCTYPE html>
                <html lang = "en">
                <head>
                <meta charset = "utf-8" >
                  <title>Medium Level</title >
                </head >
                <body style="background-color:violet;">
                """

                contents += f"""<p> The sequence of the gene {gene} is: </p>"""
                contents += f"<textarea readonly rows = 20 cols = 80>{s}</textarea>"

                contents += f"""<p><a href="/">Main page </a></body></html>"""
                status = 200

            except ValueError:
                contents = Path("Error.html").read_text()
                status = 404
            except KeyError:
                contents = Path("Error.html").read_text()
                status = 404

        elif arg0 == "/geneInfo":
            try:
                s = argument[1]
                gene = s.split("=")[1]
                Endpoint = f"/xrefs/symbol/homo_sapiens/{gene}"
                conn = http.client.HTTPConnection(Server)
                conn.request("GET", Endpoint + Parameters)
                r1 = conn.getresponse()
                data1 = r1.read().decode("utf-8")
                d1 = json.loads(data1)
                d = d1[0]
                idd = d["id"]
                Endpoint_ = f"lookup/id/{idd}"
                conn = http.client.HTTPConnection(Server)
                conn.request("GET", Endpoint_ + Parameters)
                r2 = conn.getresponse()
                d2 = r2.read().decode("utf-8")
                d_ = json.loads(d2)
                start = d_["start"]
                end = d_["end"]
                length = d_["end"]-d_["start"]
                id = d_["id"]
                chrom = d_["seq_region_name"]
                contents = """
                <!DOCTYPE html>
                <html lang = "en">
                <head>
                <meta charset = "utf-8" >
                  <title>Medium Level</title >
                </head >
                <body style="background-color:violet;">
                """


                contents += f"""<h1>  {gene} </h1>"""
                contents += f"""<p> The start of the gene is {start} </p>"""
                contents += f"""<p> The end of the gene is {end}  </p>"""
                contents += f"""<p> The length of the gene is {length}  </p>"""
                contents += f"""<p> The id of the gene is {id}  </p>"""
                contents += f"""<p> The chromosome of the gene is {chrom}"""


                contents += f"""<p><a href="/">Main page </a></body></html>"""
                status = 200

            except ValueError:
                contents = Path("Error.html").read_text()
                status = 404
            except KeyError:
                contents = Path("Error.html").read_text()
                status = 404

        elif arg0 == "/geneCalc":
            try:
                s = argument[1]
                gene = s.split("=")[1]
                Endpoint = f"/xrefs/symbol/homo_sapiens/{gene}"
                conn = http.client.HTTPConnection(Server)
                conn.request("GET", Endpoint + Parameters)
                r1 = conn.getresponse()
                data1 = r1.read().decode("utf-8")
                d1 = json.loads(data1)
                d = d1[0]
                idd = d["id"]
                Endpoint_ = f"sequence/id/{idd}"
                conn = http.client.HTTPConnection(Server)
                conn.request("GET", Endpoint_ + Parameters)
                r2 = conn.getresponse()
                d2 = r2.read().decode("utf-8")
                d_ = json.loads(d2)
                seq = d_["seq"]
                sequence = Seq(seq)
                length = sequence.len()

                contents = """
                <!DOCTYPE html>
                <html lang = "en">
                <head>
                <meta charset = "utf-8" >
                  <title>Medium Level</title >
                </head >
                <body style="background-color:violet;">
                """
                contents += f"""<h1>  {gene} </h1>"""
                contents += f"""<p> The total length is {length}"""

                for base in all_bases:
                    count = sequence.count_base(base)
                    c.append(count)
                    percentage = (count / length) * 100
                    p.append(f"{round(percentage, 3)}")
                contents += f"""<p>{all_bases[0]}: {c[0]} : {p[0]} %</p>"""
                contents += f"""<p>{all_bases[1]}: {c[1]} : {p[1]} %</p>"""
                contents += f"""<p>{all_bases[2]}: {c[2]} : {p[2]} %</p>"""
                contents += f"""<p>{all_bases[3]}: {c[3]} : {p[3]} %</p>"""

                contents += f"""<p><a href="/">Main page </a></body></html>"""
                status = 200


            except ValueError:
                contents = Path("Error.html").read_text()
                status = 404
            except KeyError:
                contents = Path("Error.html").read_text()
                status = 404

        elif arg0 == "/geneList":
            try:
                s = argument[1]
                ch = s.split('&')[0]
                st = s.split('&')[1]
                en = s.split('&')[2]
                chromo = ch.split("=")[1]
                start = st.split("=")[1]
                end = en.split("=")[1]
                Endpoint = f"overlap/region/human/{chromo}:{start}-{end}"
                Parameter = '?feature=gene;content-type=application/json'
                conn = http.client.HTTPConnection(Server)
                conn.request("GET", Endpoint + Parameter)
                r1 = conn.getresponse()
                data1 = r1.read().decode("utf-8")
                d1 = json.loads(data1)
                contents = """
                                    <!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                    <meta charset = "utf-8" >
                                      <title>Medium Level</title >
                                    </head >
                                    <body style="background-color:violet;">
                                    """

                for i in d1:
                    contents += f"""<p> * {i["external_name"]} </p>"""

                contents += f"""<p><a href="/">Main page </a></body></html>"""
                status = 200

            except ValueError:
                contents = Path("Error.html").read_text()
                status = 404
            except KeyError:
                contents = Path("Error.html").read_text()
                status = 404


        self.send_response(status)

        # Define the content-type header:
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return

Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()