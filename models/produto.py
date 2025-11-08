import json

class Produto:
    def __init__(self, id: int, d: str, p: float, e: int, Categoria):
        self._id = id
        self.descricao = d
        self.preco = p
        self.estoque = e
        self.idCategoria = Categoria

    def __str__(self):
        if self.idCategoria:
            categoria_resposta = self.idCategoria
        else:
            categoria_resposta = 'Sem Categoria'
        return f"Id: {self._id} \nDescrição: {self.descricao} \nPreço: {self.preco} \nEstoque: {self.estoque} \nCategoria: {categoria_resposta}"

class ProdutoDAO:
    objetos = []

    @classmethod
    def inserir(cls, obj: Produto):
        id = 0
        for ver in cls.objetos:
            if ver._id > id:
                id = ver._id
        obj._id = id + 1  
        cls.objetos.append(obj)
          
    @classmethod
    def listar(cls):
        return cls.objetos

    @classmethod
    def listar_id(cls, id: int):
        for obj in cls.objetos:
            if obj._id == id:  
                return obj
        raise ValueError("ID Produto não encontrado")

    @classmethod
    def atualizar(cls, obj: Produto):
        for i, produto in enumerate(cls.objetos):  
            if produto._id == obj._id:  
                cls.objetos[i] = obj
                return cls.objetos
        raise ValueError("Não foi achado o ID")

    @classmethod
    def excluir(cls, obj: Produto):
        for i, produto in enumerate(cls.objetos): 
            if produto._id == obj._id:  
                del cls.objetos[i]
                return cls.objetos
        raise ValueError("Não foi encontrado ID")

    @classmethod
    def salvar(cls):
        with open('produto.json', 'w') as arquivo:  
            json.dump([obj.__dict__ for obj in cls.objetos], arquivo)
    
    @classmethod
    def abrir(cls):
        try:
            with open('produto.json', 'r') as arquivo: 
                dados = json.load(arquivo)
                cls.objetos = [Produto(d['_id'], d['descricao'], d['preco'], d['estoque'], d['idCategoria']) for d in dados]  # CORRIGIR: fechar parênteses corretamente
        except FileNotFoundError:
            cls.objetos = []
