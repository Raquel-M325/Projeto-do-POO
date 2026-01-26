import streamlit as st
import pandas as pd
from view import View
import time

class MaisVendidosUI:
    def main():
        st.header("Produtos mais vendidos")
        tab1, = st.tabs(["Reclamar"])
        with tab1:MaisVendidosUI.mais_vendidos()

    def mais_vendidos():
        