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
        tok += char
        if tok == " ":
            tok =""
        elif tok=="bhala":
            tok=""
        elif tok=="\"" and state==0:
            state = 1      
            tok=""

        elif tok =="\"" and state ==1:
            print(string)
            state =0
            string =""

        elif state == 1:
            string+=char
            tok=""       
def run():
    data = open_file(argv[1])
    lex(data)
run()
