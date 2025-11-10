from models.categoria import Categoria, CategoriaDAO
from models.cliente import Cliente, ClienteDAO
from models.produto import Produto, ProdutoDAO
from models.venda import Venda, VendaDAO
from models.vendaitem import VendaItem, VendaItemDAO

class View:

    def cliente_criar_admin():
        # cria o usuário admin se ele não existir
        for obj in View.cliente_listar():
            if obj.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "1234", "1234") 

    def cliente_autenticar(email, senha):
        for obj in View.cliente_listar():
            if obj.get_email() == email and obj.get_senha() == senha: 
                return { "id": obj.get_id(), "nome": obj.get_nome() }
        return None



    def cliente_inserir(nome, email, fone):
        id = 0
        c = Cliente(id, nome, email, fone)
        ClienteDAO.inserir(c) #instanciar DAO vai criar várias listas de clientes
    
    def cliente_listar():
        return ClienteDAO.listar()
    
    def cliente_atualizar(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(c)
    
    def cliente_excluir(id):
        nome = ""
        email = ""
        fone = ""
        c = Cliente(id, nome, email, fone)
        ClienteDAO.excluir(c)

    def categoria_inserir(descricao):
        id = 0
        c = Categoria(id, descricao)
        CategoriaDAO.inserir(c)
    
    def categoria_listar():
        return CategoriaDAO.listar()
    
    def categoria_atualizar(id, descricao):
        c = Categoria(id, descricao)
        CategoriaDAO.atualizar(c)
    
    def categoria_excluir(id):
        descricao = ""
        c = Categoria(id, descricao)
        CategoriaDAO.excluir(c)
    
    def produto_inserir(descricao, preco, estoque, id_Categoria):
        id = 0
        c = Produto(id, descricao, preco, estoque, id_Categoria)
        ProdutoDAO.inserir(c)
    
    def produto_listar():
        return ProdutoDAO.listar()

    def produto_atualizar(id, descricao, preco, estoque, id_Categoria):
        c = Produto(id, descricao, preco, estoque, id_Categoria)
        ProdutoDAO.atualizar(c)
    
    def produto_excluir(id):
        descricao = ""
        preco = 0
        estoque = 0
        id_Categoria = 0
        c = Produto(id, descricao, preco, estoque, id_Categoria)
        ProdutoDAO.excluir(c)
    
    def reajustar_preco(porcentagem):
        for obj in ProdutoDAO.listar():
            obj.reajustar_preco()
            ProdutoDAO.atualizar(obj)
    
    # SERÁ COLOCADO DEPOIS!!!!! AINDA FALTA MONTAR A INTERAÇÃO DESSA PARTE DO SISTEMA.

    # def venda_inserir():
    
    # def venda_listar():
    #     return VendaDAO.listar()
    
    # def venda_atualizar():
    
    # def venda_excluir():
    
    # def vendaitem_inserir():
    
    # def vendaitem_listar():
    #     return VendaItemDAO.listar()

    # def vendaitem_atualizar():
    
    # def vendaitem_excluir():
