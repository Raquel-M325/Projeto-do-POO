import streamlit as st
from view import View
import pandas as pd

class ListarVendasUI:
    def main():
        st.header("Lista dos Pedidos Realizados")
        tab1, = st.tabs(["Listar"])
        with tab1: ListarVendasUI.listar()

    def listar():
        vendas = View.chec_vendas()
        if len(vendas) == 0: st.write("Nenhuma venda foi realizada")
        else:   
            list_dic = []
            for obj in vendas: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["produto", "qtd", "preco", "id_Venda"] )
