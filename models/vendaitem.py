import json

class VendaItem:
    def __init__(self, id: int, q: int, p: float, Venda, Produto):
        self._id = id
        self.qtd = q
        self.preco = p
        self.IdVenda = Venda
        self.idProduto = Produto

    def __str__(self):
        if self.idProduto:
            produto_resposta = self.idProduto
        else:
            produto_resposta = "Sem Produto"
        if self.IdVenda:
            venda_resposta = self.IdVenda
        else:
            venda_resposta = "Sem Venda"
        return f"Id: {self._id} \nQuantidade: {self.qtd} \nPreço: {self.preco} \nVenda: {venda_resposta} \nProduto: {produto_resposta}"

class VendaItemDAO:
    objetos = []

    @classmethod
    def inserir(cls, obj: VendaItem):
        id = 0
        for ver in cls.objetos:
            if ver._id > id:
                id = ver._id
        obj._id = id + 1    # tem que especificar o obj para verificar no VendaItem que irá usar, nesse caso será o id dele
        cls.objetos.append(obj)
    
    @classmethod
    def listar(cls):
        return cls.objetos
    
    @classmethod
    def listar_id(cls, id: int):
        for obj in cls.objetos:
            if obj._id == id:
                return obj
        raise ValueError('o ID VendaItem não foi encontrado')
    
    @classmethod
    def atualizar(cls, obj: VendaItem):
        for i, vendaitem in enumerate(cls.objetos):
            if vendaitem._id == obj._id:
                cls.objetos[i] = obj
                return cls.objetos
        raise ValueError('Não foi achado o ID')
    
    @classmethod
    def excluir(cls, obj: VendaItem):
        for i, vendaitem in enumerate(cls.objetos):
            if vendaitem._id == obj._id:
                del cls.objetos[i]
                return cls.objetos
        raise ValueError('Não foi encontrado ID')

    @classmethod
    def salvar(cls):
        with open('vendaitem.json', 'w') as arquivo:
            json.dump([obj.__dict__ for obj in cls.objetos], arquivo)

    @classmethod
    def abrir(cls):
        try:
            with open('vendaitem.json', 'r') as arquivo:
                dados = json.load(arquivo)
                cls.objetos = [VendaItem(d['_id'], d['qtd'], d['preco'], d.get('IdVenda'), d.get('idProduto')) for d in dados]
        except FileNotFoundError:
            cls.objetos = []
