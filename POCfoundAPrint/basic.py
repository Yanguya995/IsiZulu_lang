from sys import *

def open_file(filename):
   data = open(filename, "r").read()   
   return data

def lex(filecontents):
    tok =""    
    state = 0
    string = ""
    filecontents = list(filecontents)
    for char in filecontents:
        tok+=char
        if tok=="bhala":
            print("Found a print")
            tok=""      
def run():
    data = open_file(argv[1])
    lex(data)
run()
