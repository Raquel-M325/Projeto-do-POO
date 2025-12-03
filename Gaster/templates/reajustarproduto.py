import streamlit as st
import pandas as pd
from view import View
import time

class ReajustarProdutoUI:
    def main():
        st.header("Reajustar Preços de Produtos")
        tab1 = st.tabs(["Reajustar"])
        with tab1: ReajustarProdutoUI.reajustar()

    def reajustar():
        preco = st.text_input("Informe o preço a ser reajustado")
        if st.button("Reajustar"):
            View.reajustar_preco(preco)
            st.success("Preço atualizado com sucesso")
            time.sleep(2)
            st.rerun()