import json
from models.dao import DAO
from models.cliente import Cliente
from models.produto import Produto

class Entrega:
    def __init__(self, id, idCliente, descricao_entrega):
        self.set_id(id)
        self.set_idCliente(idCliente)
        self.set_descricao(descricao_entrega)

    def set_id(self, id):
        self.id = id

    def set_descricao(self, descricao_entrega):
        self.descricao_entrega = descricao_entrega

    def set_idCliente(self, idCliente):
        self.idCliente = idCliente

    def get_id(self): return self.id
    def get_descricao(self): return self.descricao_entrega
    def get_idCliente(self): return self.idCliente

    def __str__(self):
        return f'Id do entrega: {self.id} - Descrição da entrega: {self.descricao_entrega} - Id do Cliente: {self.idCliente}'

    def to_json(self):
        return { "id" : self.id, "descricao_entrega" : self.descricao_entrega, "idCliente" : self.idCliente }
    def from_json(dic):
        return entrega(dic["id"], dic["descricao_entrega"], dic["idCliente"])


class EntregaDAO(DAO):
    @classmethod
    def salvar(cls):
        with open("entrega.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = entrega.to_json, indent = 4)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("entrega.json", mode = "r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = entrega.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass