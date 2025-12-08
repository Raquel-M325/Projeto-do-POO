import streamlit as st
from view import View
import pandas as pd

class ListarPedidosRealizadosUI:
    def main():
        st.header("Lista dos Pedidos Realizados")
        tab1 = st.tabs(["Listar"])
        try:
            ListarPedidosRealizadosUI.listar()
        
        except:
            print("Não há pedidos realizados, ainda há produtos no carrinho que não foram comprados!")


    def listar():
        carrinho = View.venda_listar.listar()
        if len(carrinho) == 0: st.write("Nenhuma pedido foi realizado")
        else:   
            list_dic = []
            for obj in carrinho: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "quantos", "preco", "id_Venda", "id_Produto"] )

