import json
# from models.produto import ProdutoDAO
# from models.venda import VendaDAO
class VendaItem:
    def __init__(self, id, qtd, preco, id_Venda, id_Produto):
        self.set_id(id)
        self.set_qtd(qtd)
        self.set_preco(preco)
        self.set_idVenda(id_Venda)
        self.set_idProduto(id_Produto)

    #Set
    def set_id(self, id):
        self.id = id
    def set_qtd(self, qtd):
        if qtd <= 0: raise ValueError("Digite uma quantidade válida! ")
        self.qtd = qtd
    def set_preco(self, preco):
        self.preco = preco
    def set_idVenda(self, id_Venda):
        self.idVenda = id_Venda
    def set_idProduto(self, id_Produto):
        self.idProduto = id_Produto
    
    #Get
    def get_id(self): return self.id
    def get_qtd(self): return self.qtd
    def get_preco(self): return self.preco
    def get_idVenda(self): return self.idVenda
    def get_idProduto(self): return self.idProduto


    def __str__(self):
        return f"Id: {self.id} - Quantidade: {self.qtd} - Preço: {self.preco:.2f} - Id de Venda: {self.idVenda} - Id do Produto: {self.idProduto}"
    def to_json(self):
        return { "id" : self.id, "qtd" : self.qtd, "preco" : self.preco, "id_Venda" : self.idVenda, "id_Produto" : self.idProduto }
    def from_json(dic):
        return VendaItem(dic["id"],  dic["qtd"], dic["preco"], dic["id_Venda"], dic["id_Produto"])
    
class VendaItemDAO:
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
        aux = cls.lista_id(obj.id)
        if aux != None:
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
        with open("vendaitem.json", mode="w") as arquivo:
            #json.dump(cls.objetos, arquivo, default = vars, indent=4)
            json.dump(cls.objetos, arquivo, default = VendaItem.to_json, indent=4)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("vendaitem.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    # c = Cliente(dic["id"], dic["nome"])
                    c = VendaItem.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass