import json

'''
Une classe pour tester
https://realpython.com/python-pep8/
'''
class Classe:
    def __init__(self,a:str,b:str) -> None:
        self.nom=a
        self.prenom=b
        

    def toJson(self):
        # storing the JSON response from url in data
        return json.loads('{ "name":"'+self.nom+'", "prenom":"'+self.prenom+'"}')

    def toJsone(self):        
        x={
            "name": self.nom,
            "age": self.prenom,
        }
        return json.dumps(x, indent=4)

        
#test

t=Classe("Renaud","graougrr")

print(json.dumps(t.toJson()))
#print(t.toJsone())
#print(type(t.toJsone()))