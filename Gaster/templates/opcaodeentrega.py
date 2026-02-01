import streamlit as st
import pandas as pd
from view import View
import time

class OpcaodeEntregaUI:
    def main():
        st.header("Opções de entrega")
        tab1, = st.tabs(["Escolha a entrega"])
        with tab1: OpcaodeEntregaUI.forma_entrega()

    def forma_entrega():
        opcaoentrega = st.number_input("Digite o 1 para domicílio e 2 para local.", min_value=0, max_value=3, step = 0)
        if opcaoentrega == 1: descricao = OpcaodeEntregaUI.domicilio()
        if opcaoentrega == 2: descricao = OpcaodeEntregaUI.local()
        if st.button("Comprar"):
            View.entrega_inserir(st.session_state["cliente_id"], descricao)
            st.success("Confirmado! Seu produto será entregue!")
            time.sleep(2)
            st.rerun()

    def domicilio():
        st.write("========= ENTREGA DOMICILIO ESCOLHIDA =========")
        nome = st.text_input("Nome Completo: ")
        telefone = st.number_input("Telefone: ")
        endereco = st.number_input("Endereço do CEP: ") #podemos detalhar mais o endereço, mas quis simplificar
        descricao = "Domicílio"
        return descricao

    def local():
        st.write("========= ENTREGA LOCAL ESCOLHIDA =========")
        nome = st.text_input("Nome Completo: ")
        telefone = st.number_input("Telefone: ")
        data = st.number_input("Data para buscar: ") #precisa avaliar se é ideal ter esse
        descricao = "Local"
        return descricao