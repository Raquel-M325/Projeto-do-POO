from abc import ABC, abstractmethod

class Figura3D(ABC):
    @abstractmethod
    def getvolume(self):
        pass

class Esfera(Figura3D):
    def __init__(self, raio):
        self.__raio = raio

    def getvolume(self):
        return self.__raio**3 * 3,14 * 4/3

class Cubo(Figura3D):
    def __init__(self, lado):
        self.__lado = lado
    def getvolume(self):
        return self.__lado**3

x = Cubo(7)
y = Esfera(5)

print(x.getvolume())
print(y.getvolume())
