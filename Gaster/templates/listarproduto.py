import streamlit as st
import time
from view import View
import pandas as pd

class ListarProdutoUI:
    def main():
        st.header("Lista de Produtos")
        tab1, = st.tabs(["Listar"])
        with tab1:ListarProdutoUI.listar()

    def listar():
        produto = View.produto_listar()
        if len(produto) == 0: st.write("Nenhum Produto cadastrado")
        else:
            list_dic = []
            for obj in produto: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["descricao", "preco", "estoque"])
