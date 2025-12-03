import streamlit as st
from view import View

class AbrirUI:
    def main():
        st.header("Criar conta")
        nome = st.text_input("Digite seu nome")
        email = st.text_input("Informe seu e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe sua senha", type ="password")
        if st.button("Criar"):
            c = View.cliente_inserir(nome, email, fone, senha)
            st.rerun()