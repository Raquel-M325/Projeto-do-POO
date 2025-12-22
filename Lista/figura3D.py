from abc import ABC, abstractmethod

class Figura3D(ABC):
    @abstractmethod
    def getvolume(self):
        pass

class Esfera(Figura3D):
    def __init__(self, raio: float):
        self.setraio(raio)

    def setraio(self, raio):
        if not isinstance(raio, (float, int)):
            raise ValueError('Não é número, digite um válido')

        if raio < 0:
            raise ValueError('Número negativo!')

        self.__raio = raio

    def getraio(self):
        return self.__raio

    def getvolume(self):
        return self.__raio**3 * 3.14 * 4/3

class Cubo(Figura3D):
    def __init__(self, lado):
        self.setlado(lado)

    def setlado(self, lado):
        if not isinstance(lado, (float, int)):
            raise ValueError('Não é número, digite um válido')

        if lado < 0:
            raise ValueError('Número negativo!')

        self.__lado = lado

    def getlado(self):
        return self.__lado

    def getvolume(self):
        return self.__lado**3

x = Cubo(7)
y = Esfera(5)

print(x.getvolume())
print(y.getvolume())
