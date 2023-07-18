import math

class nombre_complexe:
    def __init__(self, a=0, b=0):
        self.a, self.b = a, b

    def get_module(self):
        return math.sqrt(self.a * self.a + self.b * self.b)

    def ajoute(self, c):
        return nombre_complexe(self.a + c.a, self.b + c.b)


c1 = nombre_complexe(0, 1)
c2 = nombre_complexe(1, 0)

c = c1.ajoute(c2)         # c = c1 + c2
print(c.a, c.b)