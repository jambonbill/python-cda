#https://docs.python.org/fr/3/library/os.html
import os

#os.chdir(path)
#os.fchdir(fd)
#os.getcwd()

def encode(str:str,shift:int):
    print('encode()')
    
    output=''
    for letter in str:
        n=ord(letter)
        output+=chr(n+shift)

    return output

def saveSecret(output:str):
    f=open("data/coded.txt","w")
    f.write(output)
    f.close()

inputFile="data/secret.txt"

if os.path.exists(inputFile):
    f = open("data/secret.txt", "r")
    line=f.read()
    code=encode(line,2)
    print(code)
    saveSecret(code)
else:
    print("Le fichier " + str(inputFile) + " ne pas exisdter")

