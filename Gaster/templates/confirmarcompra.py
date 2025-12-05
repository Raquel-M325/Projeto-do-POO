import streamlit as st
from view import View
import pandas as pd

class ConfirmarCarrinhoUI:
    def main():
        st.header("Confirmação de Compra")
        st.session_state["cliente_id"] = c["id"]
        pagar = st.text_input("Informe a opção do pagamento: ")
        if st.button("Confirmar"):
            if View.opcao_pagar(pagar) != None: 
                st.write("Carrinho confirmado! Compra com sucesso!")
            else:
                st.write("Compra não foi executada, ainda há carrinho com os produtos")
                st.rerun()