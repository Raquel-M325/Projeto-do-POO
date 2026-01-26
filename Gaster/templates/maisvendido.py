import streamlit as st
from view import View
import pandas as pd


class MaisVendidoUI:
    def main():
        st.header("lista das vendas mais vendidos")

    def listar():
        produto = View.listar_vendas()
        if len(produto) == 0: st.write("Não teve venda nem compra dos produtos")
        else:
            list_dic = []
            for obj in produto: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "qtd"])        

    def maior():
        




    