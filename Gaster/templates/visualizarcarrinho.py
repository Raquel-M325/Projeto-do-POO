import streamlit as st
import time
from view import View
import pandas as pd

class VisualizarCarrinhoUI:
    def main():
        st.header("Carrinho")
        tab1 = st.tabs(["visualizar"])
        try:
            VisualizarCarrinhoUI.visualizar()

        except:
            st.write("Nenhum produto no carrinho")


    def visualizar():
        venda = View.venda_existente(st.session_state["cliente_id"])
        itens = View.visualizar_carrinho(venda)
        if len(itens) == 0: st.write("Seu carrinho não tem produtos")
        else:
            list_dic = []
            for i in range(len(itens)): list_dic.append(itens[i])
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id_Produto", "qtd", "preco"])      