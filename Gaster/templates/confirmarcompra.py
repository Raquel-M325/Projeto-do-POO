import streamlit as st
from view import View
import pandas as pd

class ConfirmarCarrinhoUI:
    def main():
        st.header("Confirmação de Compra")
        if View.comprar_carrinho() != None: print("Carrinho confirmado! Compra com sucesso!")
        else:
            print("Compra não foi executada, ainda há carrinho com os produtos")
