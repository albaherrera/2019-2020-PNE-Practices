import http.server
import socketserver
from pathlib import Path

import termcolor

from P1.Seq1 import Seq

# Define the Server's port and the folder
PORT = 8080
FOLDER = "../Session-04/"

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

        # Define the sequences that we are going to use in "get" and the bases for exercise 4
        sequence = ["GTAGCA", "ACGTTA", "CGTAGG", "ATTGTC"]
        all_bases = ["A","C","G","T"]

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

        # All the information appears in "form-4.html"
        if arg0 == "/":
            contents = Path("form-4.html").read_text()
            status = 200
        elif arg0 == "/ping":
            contents = """
            <!DOCTYPE html>
            <html lang = "en">
            <head>
            <meta charset = "utf-8" >
              <title> ping </title >
            </head >
            <body>
            <h2> PING ok!</h2>
            <p> The SEQ2 Server in running... </p>
            <a href="/">Main page</a>
            </body>
            </html>
            """
            status = 200
        elif arg0 == "/get":

            # We define our second argument, the one after the "?" that we have split.
            arg1 = argument[1]

            # To split the "&" that is after the value
            args = arg1.split("&")

            # Is necessary to split the "=" after our name ("msg")
            name,value = args[0].split("=")

            # We define the argument n
            n = int(value)
            seq = sequence[n-1]
            contents = f"""
            <!DOCTYPE html>
            <html lang = "en">
            <head>
            <meta charset = "utf-8" >
              <title> get </title >
            </head >
            <body>
            <h2>Sequence number {n}</h2>
            <p> {seq}</p>
            <a href="/">Main page</a>
            </body>
            </html>
            """
            status = 200
        elif arg0 == "/gene":
            # We define our second argument, the one after the "?" that we have split.
            arg1 = argument[1]

            # To split the "&" that is after the value
            args = arg1.split("&")

            # Is necessary to split the "=" after our name ("msg")
            name,gene_name = args[0].split("=")

            # Sequence of the gene
            s = Seq()
            s_string = str(s.read_fasta(FOLDER+gene_name))
            contents = f"""
            <!DOCTYPE html>
            <html lang = "en">
            <head>
            <meta charset = "utf-8" >
              <title> gene </title >
            </head >
            <body>
            <h2>Gene {gene_name}</h2>
            <textarea readonly rows="20" cols="80"> {s_string} </textarea>
            <a href="/">Main page</a>
            </body>
            </html>
            """
            status = 200

        elif arg0 == "/operation":
            # We define our second argument, the one after the "?" that we have split.
            arg1 = argument[1]

            # To split the "&" that is after the value
            args = arg1.split("&")

            # Name and values (=arguments)
            #seq in order to create the sequence
            name,seq = args[0].split("=")
            #op are the different options that can be chosen after the sequence is written
            name,op = args[1].split("=")

            #Introduce the sequence
            s = Seq(seq)


            if "info" in op:
                s = Seq(seq)
                s_length = s.len()
                list1 = []
                list2 = []

                for b in all_bases:

                    count_b = s.count_base(b)
                    p = round(count_b * (100 / s_length), 1)  # percentage calculation with just 1 decimal
                    list1.append(count_b) # list 1: where we put the total bases
                    list2.append(p) # list2 : where we put the percentage of all the bases


                response = f"""
                Total length: {s_length}
                <p>A: {list1[0]} ({list2[0]}%)</p>
                <p>C: {list1[1]} ({list2[1]}%)</p>
                <p>G: {list1[2]} ({list2[2]}%)</p>
                <p>G: {list1[3]} ({list2[3]}%)</p>
                
                """

            elif "comp" in op:
               response = s.complement()

            elif "rev" in op:
                response = s.reverse()

            contents = f"""
            <!DOCTYPE html>
            <html lang = "en">
            <head>
            <meta charset = "utf-8" >
              <title> operation </title >
            </head >
            <body>
            <h2>Sequence :</h2>
            <p>{seq}</p>
            <h2>Operation :</h2>
            <p>{op}</p>
            <h2>Result :</h2>
            <p>{response}</p>
            <a href="/">Main page</a>
            </body>
            </html>
            """
            status = 200




        else:
            # Error.html file
            contents = Path("Error.html").read_text()
            status = 404

        # Generating the response message
        self.send_response(status)

        # Define the content-type header:
        self.send_header('Content-Type',content_type)
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
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