
from typing import List

from P1.Seq1 import Seq
import socket
import termcolor

IP = "127.0.0.1"
PORT = 40974
FOLDER ="../Session-04/"
FILENAMES = ["U5","FRAT1","ADA","FXN","RNU6_269P"]
sequence = ["GTAGCA","ACGTTA","CGTAGG","ATTGTC"]
all_bases = ["A","C","G","T"]

def ping():
    print(f"OK!")

def get(n):
    print (f"{sequence[n]}")

def info(seq):
    s = Seq(seq)
    s_length = s.len()
    counter_A = s.count_base(all_bases[0])
    counter_C = s.count_base(all_bases[1])
    counter_G = s.count_base(all_bases[2])
    counter_T = s.count_base(all_bases[3])
    per_A = "{:.1f}".format(100 * counter_A / s_length)
    per_C = "{:.1f}".format(100 * counter_C / s_length)
    per_G = "{:.1f}".format(100 * counter_G / s_length)
    per_T = "{:.1f}".format(100 * counter_T / s_length)

    response_message = f"""Sequence: {s}
    f"Total length: {s_length}"
    A: {counter_A} ({per_A}%)
    C: {counter_C} ({per_C}%)
    G: {counter_G} ({per_G}%)
    T: {counter_T} ({per_T}%)"""
    return response_message

def comp (seq):
    s = Seq(seq)
    return s.complement()

def rev (seq):
    s = Seq(seq)
    return s.reverse()

def gene (name):
    s = Seq()
    s.read_fasta(FOLDER + FILENAMES)
    return s




#Create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Link IP and PORT
ls.bind((IP, PORT))

# Listening if there are clients
ls.listen()
print("SEQ server configured!")

while True:
    print("Waiting for Clients...")
    try:
        (cs, client_ip_port) = ls.accept()

    #  Server stopped by the user
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # Close the listenning socket and exit
        ls.close()
        exit()

    else:

        print("A client has connected to the server!")

        # Recieve the msg (bytes)
        msg_raw = cs.recv(2048)

        # Decode the msg for reading it
        msg = msg_raw.decode()

        # Separate argument and command
        lines = msg.split("\n")
        line = lines[0].strip()
        com_arg = line.split(" ")
        command = com_arg[0]

        try:
            argument = com_arg[1]

        # Index Errors when there aren't response and argument
        except IndexError:
            response = " "
            argument = " "

        if "PING" in command:
            response = "OK!\n"
            termcolor.cprint("PING command!","green")
        elif "GET" in command:
            response = get(int(argument))
            termcolor.cprint("GET","green")
        elif "INFO" in command:
            response = info(argument)
            termcolor.cprint("INFO", "green")
        elif "COMP" in command:
            response =comp(argument)
            termcolor.cprint("COMP", "green")
        elif "REV" in command:
            response = rev(argument)
            termcolor.cprint("GENE", "green")
        elif "GENE" in command:
            response = gene(argument)
            termcolor.cprint("GENE", "green")
        else:
            response = "Try again"

        #print the response deppending on the command selected
        response += '\n'
        print(response)
        cs.send(response.encode())
        cs.close()







