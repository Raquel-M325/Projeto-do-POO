import json
class Venda:
    def __init__(self, id, data, carrinho, total, id_Cliente):
        self.id = id
        self.data = data
        self.carrinho = carrinho
        self.total = total
        self.id_Clientes = id_Cliente
    
    def __str__(self):
        return f"{self.id} - {self.data} - {self.carrinho} - {self.total} - {self.id_Cliente}"
    def to_json(self):
        return { "id" : self.id, "data" : self.data, "total" : self.total, "id_Cliente" : self.id_Cliente }
    def from_json(dic):
        return Venda(dic["id"], dic["data"], dic["carrinho"], dic["total"], dic["id_Cliente"])

class VendaDAO:
    objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.abri()
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