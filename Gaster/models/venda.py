import json
from models.vendaitem import VendaItem, VendaItemDAO
from models.cliente import ClienteDAO
from datetime import datetime
class Venda:
    def __init__(self, id, id_Cliente):
        self.set_id(id)
        self.set_data(None)
        self.set_carrinho()
        self.set_total()
        self.set_id_Cliente(id_Cliente)
    
    #Set
    def set_id(self, id):
        self.id = id
    def set_data(self, data):
        if data is None:
            self.data = datetime.now()
        else:
            self.data = data
    def set_carrinho(self):
        self.carrinho = True
    def set_total(self):
        total = 0
        for obj in VendaItemDAO.listar():
            if obj.get_idVenda() == self.id:
                total += obj.get_preco() * obj.get_qtd()
        self.total = total
         
    def set_id_Cliente(self, id_Cliente):
        self.id_Cliente = id_Cliente
    #Get
    def get_id(self): return self.id
    def get_data(self): return self.data
    def get_carrinho(self): return self.carrinho
    def get_total(self): return self.total
    def get_id_Cliente(self): return self.id_Cliente
    
    def cliente_nome(self):
        for obj in ClienteDAO.listar():
            if obj.get_id() == self.id_Cliente: 
                return obj.get_nome() 
        return 'Cliente não encontrado'


    def __str__(self):
        return f"{self.id} - {self.data.strftime('%d/%m/%Y')} - {self.carrinho} - {self.total} - {self.id_Cliente}"
    def to_json(self):
        return { "id" : self.id, "data" : self.data.strftime("%d/%m/%Y"), "total" : self.total, "id_Cliente" : self.id_Cliente }
    def from_json(dic):
        return Venda(dic["id"], \
        datetime.strptime(dic["data"], "%d/%m/%Y"), dic["carrinho"], dic["total"], dic["id_Cliente"])

class VendaDAO:
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
        with open("venda.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Venda.to_json, indent = 4)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("venda.json", mode = "r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Venda.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass