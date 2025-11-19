import json
from models.categoria import CategoriaDAO
class Produto:
    def __init__(self, id, descricao, preco, estoque, id_Categoria):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.set_id_Categoria(id_Categoria)

    
    #SET 
    def set_id(self, id):
        self.id = id
    def set_descricao(self, descricao):
        self.descricao = descricao
    def set_preco(self, preco):
        self.preco = preco
    def set_estoque(self, estoque):
        self.estoque = estoque
    def set_id_Categoria(self, id_Categoria):
        self.id_Categoria = id_Categoria
    

    #GET
    def get_id(self): return self.id
    def get_descricao(self): return self.descricao
    def get_preco(self): return self.preco
    def get_estoque(self): return self.estoque
    def get_id_Categoria(self): return self.id_Categoria
        

    def reajustar_preco(self, porcentagem):
        self.preco = self.preco * (1 + (porcentagem/100))

    def __str__(self):
        return f"Id do Produto: {self.id} - Descrição: {self.descricao} - Preço do produto: R${self.preco:.2f} - Estoque: {self.estoque} - Unidades - {self.get_id_Categoria()}"
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