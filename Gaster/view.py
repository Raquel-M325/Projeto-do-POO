from models.categoria import Categoria, CategoriaDAO
from models.cliente import Cliente, ClienteDAO
from models.produto import Produto, ProdutoDAO
from models.venda import Venda, VendaDAO
from models.vendaitem import VendaItem, VendaItemDAO
import json
from datetime import datetime

class View:

    def cliente_criar_admin():
        # cria o usuário admin se ele não existir
        for obj in View.cliente_listar():
            if obj.get_email() == "admin": return "Olá adm"
        View.cliente_inserir("admin","admin", "1234", "1234")

    def cliente_autenticar(email, senha):
        for obj in View.cliente_listar():
            if obj.get_email() == email and obj.get_senha() == senha: 
                return { "id": obj.get_id(), "nome": obj.get_nome() }
        return None


    #CLIENTE
    def cliente_inserir(nome, email, fone, senha):
        c = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(c) #instanciar DAO vai criar várias listas de clientes
    
    def cliente_listar():
        return ClienteDAO.listar()
    
    def cliente_atualizar(id, nome, email, fone, senha):
        c = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(c)
    
    def cliente_excluir(id):
        c = Cliente(id, "", "", "", "")
        ClienteDAO.excluir(c)

    #CATEGORIA
    def categoria_inserir(descricao):
        c = Categoria(0, descricao)
        CategoriaDAO.inserir(c)
    
    def categoria_listar():
        return CategoriaDAO.listar()
    
    def categoria_atualizar(id, descricao):
        c = Categoria(id, descricao)
        CategoriaDAO.atualizar(c)
    
    def categoria_excluir(id):
        c = Categoria(id, "")
        CategoriaDAO.excluir(c)


    # PRODUTO
    def produto_inserir(descricao, preco, estoque, id_Categoria):
        c = Produto(0, descricao, preco, estoque, id_Categoria)
        ProdutoDAO.inserir(c)
    
    def produto_listar():
        return ProdutoDAO.listar()

    def produto_atualizar(id, descricao, preco, estoque, id_Categoria):
        c = Produto(id, descricao, preco, estoque, id_Categoria)
        ProdutoDAO.atualizar(c)
    
    def produto_excluir(id):
        c = Produto(id, "", 0, 0, 0)
        ProdutoDAO.excluir(c)
    
    def reajustar_preco(porcentagem):
        for obj in ProdutoDAO.listar():
            obj.reajustar_preco(porcentagem)
            ProdutoDAO.atualizar(obj)
    
    #VENDA
    def venda_inserir(usuario):
        c = Venda(0, usuario)
        VendaDAO.inserir(c)

    def venda_existe(usuario):
        for obj in VendaDAO.listar():
            if obj.get_id_Cliente() == usuario:
                if obj.get_carrinho() == True: return obj.get_id()
                else: return "Venda realizada"
        View.venda_inserir(usuario)
        venda = VendaDAO.listar()[-1]
        return venda.get_id()

    def venda_existente(usuario):
        for obj in VendaDAO.listar():
            if obj.get_id_Cliente() == usuario:
                if obj.get_carrinho() == True: return obj.get_id()
                else: return "Venda realizada"
        return None

    def venda_listar():
        return VendaDAO.listar()
    
    def venda_atualizar():
        c = Venda()
        VendaDAO.atualizar(c)

    def venda_excluir(id):
        c = Venda(id)
        VendaDAO.excluir(c)
    

    # VendaItem
    def vendaitem_inserir(quantos, preco):
        c = VendaItem(0, quantos, preco)
        VendaItemDAO.inserir(c)

    def achar_preco(produto):
        for obj in ProdutoDAO.listar():
            if obj.get_id() == produto: return obj.get_preco()

    def vendaitem_listar():
        return VendaItemDAO.listar()

    def vendaitem_atualizar():
        c = VendaItem()
        VendaItemDAO.atualizar(c)

    def vendaitem_excluir(id):
        c = VendaItem(id)
        VendaItemDAO.excluir(c)


    # Funções do Cliente

    def inserir_produto(produto, quantos):
        produto_encontrado = None
        for obj in ProdutoDAO.listar():
            if obj.get_descricao() == produto:
                produto_encontrado = obj
                break

        if produto_encontrado is None:
            return "Produto não encontrado"

        quantia = produto_encontrado.get_estoque() - quantos
        if quantia < 0:
            return "Quantidade insuficiente"

        produto_encontrado.set_estoque(quantia)
        ProdutoDAO.atualizar(produto_encontrado)

        ultima_venda = VendaDAO.listar()[-1] 
        View.vendaitem_inserir(quantos, produto_encontrado.get_preco())

        
    def visualizar_carrinho(venda):
        for obj in VendaItemDAO.listar():
            if obj.get_idVenda() == venda: print(obj)


    def comprar_carrinho(pagamento, usuario):
        carrinho = False
        for obj in VendaDAO.listar():
            if obj.get_id_Cliente == usuario:
                if obj.get_carrinho() == True : obj
        return f"Seu pagamento foi realizado no {confirmacao}."

    def opcao_pagar(pagar):
        if pagar == 1: c = "Crédito" 
        if pagar == 2: c = "Débito"
        if pagar == 3: c = "Pix"
        if pagar == 4: return None
        return c
    
    def listar_minhas_compras(nome):
        for obj in ClienteDAO.listar():
            if obj.get_nome() ==  nome: n = obj.get_id()
        for obj in VendaDAO.listar():
            if obj.get_id_Cliente() == n: print(obj)