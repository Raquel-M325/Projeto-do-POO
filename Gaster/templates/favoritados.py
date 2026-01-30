import streamlit as st
from view import View
import pandas as pd
import time


class FavoritadosUI:
    def main():
        st.header("Favoritos")
        tab1, tab2 = st.tabs(["Favoritagem", "Listar Favoritos"])
        with tab1:FavoritadosUI.favoritar()
        with tab2:FavoritadosUI.favoritos()


    def favoritar():
        FavoritadosUI.listar()
        favorito = st.number_input("Digite o id do produto que gosta",value=0, step = 0)
        if st.button("Favoritar"):
            try:
                View.favoritos_inserir(st.session_state["cliente_id"], favorito)
                st.success("Novo produto favoritado")
                time.sleep(2)
                st.rerun()
            except ValueError:
                st.error("Erro de favoritagem")
                time.sleep(2)
                st.rerun()
            except KeyError:
                st.error("Você já favoritou esse produto")
                time.sleep(2)
                st.rerun()            


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
                if obj.get_idCliente() == st.session_state["cliente_id"]:
                    list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "produto", "idCliente"])

        #desfavorito = st.number_input("Digite o id do produto que queira defavoritar",value=0, step = 0)
        #if st.button("Desfavoritar"):
            #try:
                #View.favoritos_excluir(desfavorito)
                #st.success("Produto desfavoritado")
                #time.sleep(2)
                #st.rerun()
            #except:
                #st.error("Erro ao desfavoritar")
                #time.sleep(2)
                #st.rerun()

