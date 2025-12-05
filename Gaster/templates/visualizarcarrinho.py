import streamlit as st
import time
from view import View
import pandas as pd

class VisualizarCarrinhoUI:
    def main():
        st.header("Carrinho")
        tab1 = (["visualizar"])

    def visualizar():
        venda = View.venda_existente(st.session_state["cliente_id"])
        if View.visualizar_carrinho(venda)