class Frete():
    def __init__(self, d:float, p:float):
        self.setdistancia(d)
        self.setpeso(p)

    def setdistancia(self, d):
        if not isinstance(d, (int, float)):
            raise ValueError("A distância deve ser um número")
        
        if d < 0:
            raise ValueError("A distância deve ser positiva")
        
        self._distancia = d

    def setpeso(self, p):
        if not isinstance(p, (int, float)):
            raise ValueError("O peso deve ser um número")
        
        if p < 0:
            raise ValueError("O peso deve ser positivo")
        
        self._peso = p

    def getdistancia(self):
        return self._distancia
    
    def getpeso(self):
        return self._peso

    def valorfrete(self):
        return self._peso * self._distancia * 0.01

    def __str__(self):
        return f"Peso: {self._peso}; Distância = {self._distancia}; Valor do Frete = {self.valorfrete()}"

class FreteExpresso(Frete):
    def __init__(self, d:float, p:float, s:float):
        super().__init__(d, p)
        self.setseguro(s)

    def setseguro(self, s):
        if not isinstance(s, (int, float)):
            raise ValueError("O seguro deve ser um número")
        
        if s < 0:
            raise ValueError("O seguro deve ser positivo")
        
        self.__seguro = s

    def getseguro(self):
        return self.__seguro

    def valorfrete(self):
        return super().valorfrete()*2 + (0.01 * self.__seguro)

    def __str__(self):
        return f"{super().__str__()}; Seguro = {self.__seguro}" 

    # def __str__(self):
    #     return f"Peso: {self._peso}; Distância = {self._distancia}; Valor do Frete Expresso = {self.valorfrete()}; Seguro = {self.__seguro}"

x = Frete(30, 20)

y = FreteExpresso(40, 10, 30)

print(x)
print(y)
print(x.valorfrete())
print(y.valorfrete())

z = FreteExpresso(float(input()),float(input()),float(input()))
print(z.valorfrete())