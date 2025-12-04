import streamlit as st
import pandas as pd
from view import View
import time

class ReajustarProdutoUI:
    def main():
        st.header("Reajustar Preços de Produtos")
        tab1 = st.tabs(["Reajustar"])
        try:
            ReajustarProdutoUI.reajustar()
        except:
            print("Há um problema ao reajustar o produto")

    def reajustar():
        produto = View.produto_listar()
        if len(produto) == 0: st.write("Nenhum Produto pode ser reajustado")
        else:
            preco = st.text_input("Informe o preço a ser reajustado")
            if st.button("Reajustar"):
                View.reajustar_preco(preco)
                st.success("Preço atualizado com sucesso")
                time.sleep(2)
                st.rerun()