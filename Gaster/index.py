from templates.mantercategoria import ManterCategoriaUI
from templates.mantercliente import ManterClienteUI
from templates.manterproduto import ManterProdutoUI
from templates.reajustarproduto import ReajustarProdutoUI
from templates.login import LoginUI
from templates.abrir import AbrirUI
from templates.listarproduto import ListarProdutoUI
from templates.confirmarcompra import ConfirmarCarrinhoUI
from templates.inserircarrinho import InserirCarrinhoUI
from templates.listarpedidosrealizados import ListarPedidosRealizadosUI

from view import View
import streamlit as st

class IndexUI:

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", [
            "Cadastro de Categorias",
            "Cadastro de Clientes",
            "Cadastro de Produtos",
            "Reajustar Produtos"])
        #st.session_state["opcao"].append(op)
        if op == "Cadastro de Categorias": ManterCategoriaUI.main()
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Produtos": ManterProdutoUI.main()
        if op == "Reajustar Produtos": ReajustarProdutoUI.main()
        

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", [
            "Listar produtos",
            "Inserir produto no carrinho",
            "Visualizar carrinho",
            "Comprar carrinho",
            "Listar minhas compras"])
        if op == "Listar produtos": ListarProdutoUI.main()
        if op == "Inserir produto no carrinho": InserirCarrinhoUI()
        if op == "Visualizar carrinho":  VisualizarCarrinhoUI()
        if op == "Comprar carrinho": ConfirmarCarrinhoUI()
        if op == "Listar minhas compras":  ListarPedidosRealizadosUI()   
        if op == "Listar Produto": ListarProdutoUI()

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", [
            "Entrar no Sistema",
            "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirUI.main()

    def sidebar():
        if "cliente_id" not in st.session_state: IndexUI.menu_visitante()
        else:
            st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
            # usuário está logado, verifica se é o admin
            admin = st.session_state["cliente_nome"] == "admin"
            if admin: IndexUI.menu_admin()
            else: IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["cliente_id"]
            del st.session_state["cliente_nome"]
            st.rerun()

    def main():
        #if "opcao" not in st.session_state: st.session_state["opcao"] = [] 
        #st.write(st.session_state)
        # verifica a existe o usuário admin
        View.cliente_criar_admin()
        # mostrar o menu lateral
        IndexUI.sidebar()

IndexUI.main()