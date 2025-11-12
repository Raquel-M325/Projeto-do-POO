import json
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
        return f"{self.id} - {self.descricao}"
    def to_json(self):
        return { "id" : self.id, "descricao" : self.descricao }
    @staticmethod
    def from_json(dic):
        return Categoria(dic["id"], dic["descricao"])

class CategoriaDAO:                       # classe estática -> não tem instância
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