#https://docs.python.org/fr/3/library/os.html
import os

#os.chdir(path)
#os.fchdir(fd)
#os.getcwd()

def saveData(content):
    f=open("data/data.txt","w")
    f.write(content)
    f.close()