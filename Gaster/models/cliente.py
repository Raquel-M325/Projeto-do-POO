import json
class Cliente:
    def __init__(self, id, nome, email, fone, senha):

        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)
    
    #SET 
    def set_id(self, id):
        self.id = id
    def set_nome(self, nome):
        self.nome = nome
    def set_email(self, email):
        self.email = email
    def set_fone(self, fone):
        self.fone = fone
    def set_senha(self, senha):
        self.senha = senha
    
    #GET
    def get_id(self): return self.id
    def get_nome(self): return self.nome
    def get_email(self): return self.email
    def get_fone(self): return self.fone
    def get_senha(self): return self.senha


    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"
    def to_json(self):
        return { "id" : self.id, "nome" : self.nome, "email" : self.email, "fone" : self.fone, "senha" : self.senha}
    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"])

class ClienteDAO:                       # classe estática -> não tem instância
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
        with open("clientes.json", mode="w") as arquivo:
            #json.dump(cls.objetos, arquivo, default = vars, indent=4)
            json.dump(cls.objetos, arquivo, default = Cliente.to_json, indent=4)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    # c = Cliente(dic["id"], dic["nome"])
                    c = Cliente.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass