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
        if st.button("Domicílio"): OpcaodeEntregaUI.domicilio()
        if st.button("Local"): OpcaodeEntregaUI.local()
    
    def domicilio():
        st.write("========= ENTREGA DOMICILIO ESCOLHIDA =========")
        nome = number_input("Nome Completo: ")
        telefone = number_input("Telefone: ")
        endereco = number_input("Endereço do CEP: ") #podemos detalhar mais o endereço, mas quis simplificar
        return "Domicílio"

    def local():
        st.write("========= ENTREGA LOCAL ESCOLHIDA =========")
        nome = number_input("Nome Completo: ")
        telefone = number_input("Telefone: ")
        data = number_input("Data para buscar: ") #precisa avaliar se é ideal ter esse
        return "Local"