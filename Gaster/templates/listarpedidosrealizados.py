import streamlit as st
from view import View
import pandas as pd

class ListarPedidosRealizadosUI:
    def main():
        st.header("Lista dos Pedidos Realizados")
        tab1, = st.tabs(["Listar"])
        with tab1: ListarPedidosRealizadosUI.listar()

    def listar():
        venda = View.venda_feita(st.session_state["cliente_id"])
        carrinho = View.listar_minhas_compras(venda)
        if len(carrinho) == 0: st.write("Nenhuma pedido foi realizado")
        else:   
            list_dic = []
            for obj in carrinho: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["produto", "qtd", "preco", "id_Venda"] )

