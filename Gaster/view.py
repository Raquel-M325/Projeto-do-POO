from models.categoria import Categoria, CategoriaDAO
from models.cliente import Cliente, ClienteDAO
from models.produto import Produto, ProdutoDAO
from models.venda import Venda, VendaDAO
from models.vendaitem import VendaItem, VendaItemDAO
import json
import streamlit as st
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
    @staticmethod
    def venda_inserir(usuario):
        c = Venda(0, True, usuario)
        VendaDAO.inserir(c)
        return c.get_id()
        
    @staticmethod
    def venda_existe(usuario):
        for obj in VendaDAO.listar():
            if obj.get_id_Cliente() == usuario and obj.get_carrinho() is True:
                return obj.get_id()

        return View.venda_inserir(usuario)

    def venda_existente(usuario):
        for obj in VendaDAO.listar():
            if obj.get_id_Cliente() == usuario:
                if obj.get_carrinho() is True: return obj.get_id()
        return None

    def venda_feita(usuario):
        compras = []
        for obj in VendaDAO.listar():
            if obj.get_id_Cliente() == usuario:
                if obj.get_carrinho() == False: compras.append(obj.get_id()) 
            
        return compras
    
    def venda_listar():
        return VendaDAO.listar()
    
    def venda_atualizar(id, quantos, preco, id_Venda, id_Produto):
        c = Venda(id, quantos, preco, id_Venda, id_Produto)
        VendaDAO.atualizar(c)

    def venda_excluir(id):
        c = Venda(id)
        VendaDAO.excluir(c)
    

    # VendaItem
    def vendaitem_inserir(quantos, preco, id_Venda, id_Produto):
        a = 0                                                                   # Variável de verificação; Lógica do assembly ;)
        for obj in VendaItemDAO.listar():
            if obj.get_idProduto() == id_Produto and obj.get_idVenda() == id_Venda:
                soma = quantos + obj.get_qtd()
                c = VendaItem(obj.get_id(), soma, preco, id_Venda, id_Produto)
                VendaItemDAO.atualizar(c)
                a = 1
                break
        if a == 1: return
        c = VendaItem(0, quantos, preco, id_Venda, id_Produto)
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
        
    def visualizar_carrinho(venda):
        lista = []
        for obj in VendaItemDAO.listar():
            if obj.get_idVenda() == venda: lista.append(obj)
        return lista

    def comprar_carrinho(pagamento, usuario):
        for obj in VendaDAO.listar():
            if obj.get_id_Cliente() == usuario and obj.get_carrinho() is True : 
                c = Venda(obj.get_id(), False, obj.get_id_Cliente())
                # obj.get_carrinho() == False
                VendaDAO.atualizar(c)
        return f"Seu pagamento foi realizado no {pagamento}."

    def opcao_pagar(pagar):  #fiz alteraçoes para deixar mais completo
        if pagar == 1: return View.pagamento_credito() 
        if pagar == 2: return View.pagamento_debito()
        if pagar == 3: return View.pagamento_pix()
        if pagar == 4: return None
        return c

    def pagamento_credito():
        print('========================  CRÉDITO  ==========================\n')

        numero_cartao = input('Digite o número do seu cartão: ')
        validade = input('Digite a validade do cartão [MM/AA]: ')
        CVV = input('Digite o código de segurança (CVV): ')
        nome = input('Nome titular completo: ')

        return View.finalizacao()

    def pagamento_debito():
        print('===================  DÉBITO  ====================\n')

        numero_cartao = input('Digite o número do seu cartão: ')
        validade = input('Digite a validade do cartão [MM/AA]: ')
        CVV = input('Digite o código de segurança (CVV): ')
        nome = input('Nome titular completo: ')
        banco = input('Digite qual é o banco: ')
        tipo = input('Que tipo de conta (corrente ou poupança): ')

        return View.finalizacao()

    def pagamento_pix():
        print('=====================  PIX  ============================\n')

        nome = input('Nome titular completo: ')
        chave = input('Digite sua chave: ')

        return View.finalizacao()

    def finalizacao():
        return 'Espero que tenha gostado!'


    def listar_minhas_compras(vendas):
        c = []
        for obj in VendaItemDAO.listar():
            for prints in vendas:
                if obj.get_idVenda() == prints: c.append(obj)
        return c

    #ADM

    def chec_vendas():
        vendas = []
        for obj in View.venda_listar():
            if obj.get_carrinho() is False: vendas.append(obj.get_id())
        View.listar_vendas(vendas)
    
    def listar_vendas(vendas):
        for obj in VendaItemDAO.listar():
            if obj.get_idVenda() in vendas: print(obj)

    def atualizar_estoque(produto, quantos, venda, preco): #coloquei a quantidade para atualizar, mas falta ver do adm, mesmo funcionando do cliente
        for obj in ProdutoDAO.listar():
            if obj.get_id() == produto:
                novo = obj.get_estoque() - quantos
                if novo < 0: break
                obj.set_estoque(novo)
                ProdutoDAO.atualizar(obj)
                View.vendaitem_inserir(quantos, preco, venda, produto)
                break

    #Acabei criando só a ideia
    def verificar_estoque(produto):  #seria para ver a condição, caso a pessoa insista levar o estoque que está vazio, para avisar que o estoque acabou!
        for obj in ProdutoDAO.listar():
            if obj.get_id() == produto and obj.get_estoque() <= 0:
                return 'O produto está em falta!'