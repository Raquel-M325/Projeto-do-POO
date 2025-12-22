
class Retangulo:
    def __init__(self, b: float, h: float):
        self.setbase(b)
        self.setaltura(h)
        self.area = None
        self.diagonal = None

    def setbase(self, b):
        if not isinstance(b, float, int):
            raise ValueError('Não é número, digite um válido')

        if b < 0:
            raise ValueError('Número negativo!')
        
        self.setbase = b
        return self.setbase


    def setaltura(self, h):
        if not isinstance(h, float, int):
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
        return self.altura * self.base

    def calcdiagonal(self):
        return (self.altura**2 + self.base**2)**0.5
    
    def __str__(self):
        return f"O valor da área do triângulo: {self.calcarea()}\n Agora do diagonal: {self.calcdiagonal()}"


class Quadrado(Retangulo):
    def __init__(self, l):
        super().__init__(l, l)

    def setlado(self, l):
        self.setbase(l)
        self.setaltura(l)

    def getlado(self):
        return self.getbase()

    def __str__(self):
        return super().__str__()

x = Retangulo(30, 40)
y = Quadrado(20)

print(x)
print(y)
