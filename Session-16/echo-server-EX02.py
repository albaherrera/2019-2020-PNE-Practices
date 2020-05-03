import http.server
import socketserver
import termcolor
from pathlib import Path


# Define the Server's port
PORT = 8080

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

        # If the first argument is valid the "form-EX02.html" will be read
        if arg0 == "/":
            contents = Path("form-EX02.html").read_text()
            status = 200
        elif arg0 == "/echo":
            # We define our second argument, the one after the "?" that we have split.
            arg1 = argument[1]
            # To split the "&" that is after the value
            args = arg1.split("&")

            # Is necessary to split the "=" after our name ("msg")
            name,value = args[0].split("=")


            # Capital letters
            chk_value = ""
            if len(args) > 1:
                chk, chk_value = args[1].split("=")
                if chk == "chk":
                    value = value.upper()

            # And the html that appears after a word is introduced in the "form-EX02.html"
            contents = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
            </head>
            <body>
            <h2>Echoing the received message:</h2>
            <a href="/">Main page
            <body>
            <html>
            """
            print_value = f"<p>{value}</p>"
            contents+= print_value
            status = 200
        # if the first argument is different from "/" or "/echo" it will return an error
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