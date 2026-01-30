import streamlit as st
from view import View
import pandas as pd
import time


class FavoritadosUI:
    def main():
        st.header("Favoritos")
        tab1, tab2 = st.tabs(["Favoritagem", "Listar Favoritos"])
        with tab1:ReclameAquiUI.favoritar()
        with tab2:ReclameAquiUI.favoritos()


    def favoritar():
        favorito = st.number_input("Digite o id do produto que gosta")
        if button("Favoritar"):
            try:
                View.favoritos_inserir(st.session_state["cliente_id"], favorito)
                st.success("Produto inserido no carrinho com sucesso")
                time.sleep(2)
                st.rerun()
            except:
                st.error("Erro de favoritagem")
                st.rerun


    def listar():
        produto = View.produto_listar()
        if len(produto) == 0: st.write("Nenhum Produto cadastrado")
        else:
            list_dic = []
            for obj in produto: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id","descricao", "preco", "estoque"])


    def favoritos():
        favoritos = View.favoritos_listar()
        if len(favoritos) == 0: st.write("Nenhum produto favoritado")
        else:
            list_dic = []
            for obj in favoritos:
                if obj.get_idCliente() = st.session_state["cliente_id"]:
                    list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["idProduto"])

