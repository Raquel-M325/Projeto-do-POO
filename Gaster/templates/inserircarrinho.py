import streamlit as st
import time
from view import View
import pandas as pd

class InserirCarrinhoUI:
    def main():
        st.header("Insira seu item no carrinho")
        tab1 = st.tabs(["Inserir"])
        try:
            InserirCarrinhoUI.inserir()
        except:
            st.error("Nenhum produto foi inserido")

    def inserir():
        InserirCarrinhoUI.listar()
        venda = View.venda_existe(st.session_state["cliente_id"])
        produto = st.number_input("Digite o id do seu produto", value=0, step = 0, placeholder="Produto...")
        quantidade = st.number_input("Diga quantos você quer", value=0, step = 0, placeholder="Quantidade...")
        preco = View.achar_preco(produto)
        st.write(preco)
        if st.button("Inserir"):
            View.atualizar_estoque(produto, quantidade, venda, preco)
            st.success("Produto inserido no carrinho com sucesso")
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