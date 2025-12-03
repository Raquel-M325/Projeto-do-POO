import streamlit as st
import pandas as pd
from view import View
import time

class ManterProdutoUI:
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProdutoUI.listar()
        with tab2: ManterProdutoUI.inserir()
        with tab3: ManterProdutoUI.atualizar()
        with tab4: ManterProdutoUI.excluir()

    def listar():
        produto = View.produto_listar()
        if len(produto) == 0: st.write("Nenhum Produto cadastrado")
        else:
            list_dic = []
            for obj in produto: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "descricao", "preco", "estoque", "Id_Categoria"])        

    def inserir():
        try: #precisamos colocar o try e except para poder converter os valores
            descricao = st.text_input("Informe a descrição")
            preco = st.text_input(float("Informe o preco"))
            estoque = st.text_input(int("Informe o estoque"))
            id_categoria = st.text_input(int("Informe o Id da Categoria"))
            if st.button("Inserir"):
                View.produto_inserir(descricao, preco, estoque, id_categoria)
                st.success("Produto inserido com sucesso")
                time.sleep(2)
                st.rerun()

        

    def atualizar():
        produto = View.produto_listar()
        if len(produto) == 0: st.write("Nenhum Produto cadastrado")
        else:
            op = st.selectbox("Atualização de Produtos", produto)
            descricao = st.text_input("Informe a nova descrição", op.get_descricao())
            preco = st.text_input (float("Informe o novo preço", op.get_preco()))
            estoque = st.text_input (int("Informe o novo valor do estoque", op.get_estoque()))
            id_categoria = st.text_input (int("Informe o novo id da categoria", op.get_id_Categoria()))
            if st.button("Atualizar"):
                id = op.get_id()
                View.produto_atualizar(id, descricao, preco, estoque, id_categoria)
                st.success("Produto atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        produto = View.produto_listar()
        if len(produto) == 0: st.write("Nenhum Produto cadastrado")
        else:
            op = st.selectbox("Exclusão de Produtos", produto)
            if st.button("Excluir"):
                id = op.get_id()
                View.produto_excluir(id)
                st.success("Produto excluído com sucesso")
                time.sleep(2)
                st.rerun()
        
