import json
from models.dao import DAO
class Categoria:
    def __init__(self, id, descricao):
        self.set_id(id)
        self.set_descricao(descricao)

    #SET 
    def set_id(self, id):
        self.id = id
    def set_descricao(self, descricao):
        self.descricao = descricao
    
    #GET
    def get_id(self): return self.id
    def get_descricao(self): return self.descricao
    

    def __str__(self):
        return f"Id da Categoria: {self.id} - Descrição: {self.descricao}"
    def to_json(self):
        return { "id" : self.id, "descricao" : self.descricao }
    @staticmethod
    def from_json(dic):
        return Categoria(dic["id"], dic["descricao"])

class CategoriaDAO(DAO):                       # classe estática -> não tem instância
    @classmethod
    def salvar(cls):
        with open("categoria.json", mode="w") as arquivo:
            # json.dump(cls.objetos, arquivo, deafault = vars, indent=4)
            json.dump(cls.objetos, arquivo, default = Categoria.to_json, indent=4)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("categoria.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    # c = Categoria(dic["id"], dic["nome"])
                    c = Categoria.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass