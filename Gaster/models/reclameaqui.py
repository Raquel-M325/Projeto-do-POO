import json
from models.cliente import ClienteDAO
from models.dao import DAO
class Reclame:
    def __init__(self, id, reclamacao, idCliente):
        self.set_id(id)
        self.set_reclamacao(reclamacao)
        self.idCliente(idCliente)

    def set_id(self, id):
        self.id = id

    def set_reclamacao(self, reclamacao):
        self.reclamacao = reclamacao

    def set_idCliente(self, idCliente):
        self.idCliente = idCliente

    def get_id(self): return self.id
    def get_reclamacao(self): return self.reclamacao
    def get_idCliente(self): return self.idCliente

    def __str__(self):
        return f'Id do Reclame: {self.id} - Reclamação: {self.reclamacao} - Id do Cliente: {self.idCliente}'

    def to_json(self):
        return { "id" : self.id, "reclamacao" : self.reclamacao, "idCliente" : self.idCliente }
    def from_json(dic):
        return Reclame(dic["id"], dic["reclamacao"], dic["idCliente"])

class ReclameDAO(DAO):
    @classmethod
    def salvar(cls):
        with open("reclame.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Reclame.to_json, indent = 4)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("reclame.json", mode = "r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Reclame.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass