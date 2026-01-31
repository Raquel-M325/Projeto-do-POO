import json
from models.dao import DAO

class Equipe:
    def __init__(self, id, nome):
        self.set_id(id)
        self.set_nome(nome) #funcionario registrado

    def set_id(self, id):
        self.id = id

    def set_nome(self, nome):
        self.nome = nome

    def get_id(self): return self.id
    def get_nome(self): return self.nome

    def __str__(self):
        return f'Id da equipe: {self.id} - Nome do Funcionário Cadastrado: {self.nome}'

    def to_json(self):
        return { "id" : self.id, "funcionario" : self.nome}
    def from_json(dic):
        return equipe(dic["id"], dic["funcionario"],)


class equipeDAO(DAO):
    @classmethod
    def salvar(cls):
        with open("equipe.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = equipe.to_json, indent = 4)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("equipe.json", mode = "r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = equipe.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass
