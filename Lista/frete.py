class Frete():
    def __init__(self, d:float, p:float):
        self._distancia = d
        self._peso = p

    def valorfrete(self):
        return self._peso * self._distancia * 0.01

    def __str__(self):
        return f"Peso: {self._peso}; Distância = {self._distancia}; Valor do Frete = {self.valorfrete()}"

class FreteExpresso(Frete):
    def __init__(self, d:float, p:float, s:float):
        super().__init__(d, p)
        self.__seguro = s

    def valorfrete(self):
        return super().valorfrete()*2 + (0.01 * self.__seguro)

    def __str__(self):
        return f"{super().__str__()}; Seguro = {self.__seguro}" 

x = Frete(30, 20)

y = FreteExpresso(40, 10, 30)

print(x)
print(y)
print(x.valorfrete())
print(y.valorfrete())

z = FreteExpresso(float(input()),float(input()),float(input()))
print(z.valorfrete())