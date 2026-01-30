import json
from models.dao import DAO
from models.cliente import Cliente
from models.produto import Produto

class Favorito:
    def __init__(self, id, idCliente, idProduto):
        self.set_id(id)
        self.set_idProduto(idProduto)
        self.set_idCliente(idCliente)

    def set_id(self, id):
        self.id = id

    def set_idProduto(self, idProduto):
        self.idProduto = idProduto

    def set_idCliente(self, idCliente):
        self.idCliente = idCliente

    def get_id(self): return self.id
    def get_idProduto(self): return self.idProduto
    def get_idCliente(self): return self.idCliente

    def __str__(self):
        return f'Id do Favorito: {self.id} - Produto: {self.idProduto} - Id do Cliente: {self.idCliente}'

    def to_json(self):
        return { "id" : self.id, "idProduto" : self.idProduto, "idCliente" : self.idCliente }
    def from_json(dic):
        return Favorito(dic["id"], dic["idProduto"], dic["idCliente"])


class FavoritoDAO(DAO):
    @classmethod
    def salvar(cls):
        with open("favorito.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Favorito.to_json, indent = 4)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("favorito.json", mode = "r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Favorito.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass