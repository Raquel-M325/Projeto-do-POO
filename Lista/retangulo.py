import math

class Retangulo:
    def __init__(self, b: float, h: float):
        self.base = b
        self.altura = h

    def setbase(self, b):
        if not isinstance(b, float):
            raise ValueError('Não é número, digite um válido')

        if b < 0:
            raise ValueError('Número negativo!')
        
        self.base = b
        return self.base


    def setaltura(self, h):
        if not isinstance(h, float):
            raise ValueError('Não é número, digite um válido')

        if h < 0:
            raise ValueError('Número negativo!')
        
        self.altura = h
        return self.altura

    def getbase(self):
        return self.base
    
    def getaltura(self):
        return self.altura

    def calcarea(self):
        self.area = self.altura * self.base
        return self.area

    def calcdiagonal(self):
        self.diagonal = 
    
    def __str__(self):
        return f"O valor da área do triângulo: {self.area}\n Agora do diagonal: {self.diagonal}"


class Quadrado(Retangulo):
    def __init__(self, b, h):
        super().__init__(b, h)

    def __str__(self):
        return super().__str__()