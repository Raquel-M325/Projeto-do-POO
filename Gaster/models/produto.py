import json
from models.categoria import CategoriaDAO
class Produto:
    def __init__(self, id, descricao, preco, estoque, id_Categoria):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.id_Categoria = id_Categoria
        
    def get_idcat(self):
        # categoria = CategoriaDAO.listar()
        # for obj in categorias:
        #     if obj == "id":
        #         if self.id_Categoria == obj["id"]:
        #             return obj["descricao"]
        with open("categoria.json", mode="r") as arquivo:
            list_dic = json.load(arquivo)
            for dic in list_dic:
                for key in dic:
                    if key == "id":
                        if self.id_Categoria == dic[key]:
                            return dic["descricao"]
    def reajustar_preco(self, porcentagem):
        self.preco * (1 + porcentagem)

    def __str__(self):
        return f"{self.id} - {self.descricao} - R${self.preco} - {self.estoque} unidades - {self.get_idcat()}"
    def to_json(self):
        return { "id" : self.id, "descricao" : self.descricao, "preco" : self.preco, "estoque" : self.estoque, "id_Categoria" : self.id_Categoria }
    @staticmethod
    def from_json(dic):
        return Produto(dic["id"], dic["descricao"], dic["preco"], dic["estoque"], dic["id_Categoria"])
    
class ProdutoDAO:
    objetos = []                           
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.objetos:
            if aux.id > id: id = aux.id
        obj.id = id + 1 
        cls.objetos.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def lista_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id: return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        #procurar o objeto que tem o id dado por obj.id
        aux = cls.lista_id(obj.id)
        if aux != None:
            # aux.nome = obj.nome
            # remove o objeto antigo aux e insere novo obj
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        aux = cls.lista_id(obj.id)
        if aux != None:
            cls.objetos.remove(aux)
            cls.salvar()
        
    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w") as arquivo:
            #json.dump(cls.objetos, arquivo, default = vars, indent=4)
            json.dump(cls.objetos, arquivo, default = Produto.to_json, indent=4)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("produtos.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    # c = Cliente(dic["id"], dic["nome"])
                    c = Produto.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass
               


