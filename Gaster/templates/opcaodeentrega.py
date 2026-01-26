import streamlit as st
import pandas as pd
from view import View
import time

class OpcaodeEntregaUI:
    def main():
        st.header("Opções de entrega")
        tab1, = (["Escolha a entrega"])
        with tab1:OpcaodeEntregaUI.forma_entrega()

    def forma_entrega():
        