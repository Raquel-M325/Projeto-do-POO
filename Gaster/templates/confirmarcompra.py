import streamlit as st
from view import View
import pandas as pd

class ConfirmarCarrinhoUI:
    def main():
        st.header("Confirmação de Compra")
        pagar = st.text_input("Informe a opção de pagamento:")

        if st.button("Confirmar"):
            verificacao = View.opcao_pagar(pagar)

            if verificacao is not None:
                st.session_state["usuario_id"] = verificacao["id"] #acho que nessa parte esteja incompleta
                st.success("Carrinho confirmado! Compra com sucesso!")
                                st.rerun()

            else:
                st.error("Compra não foi executada. Ainda há produtos no carrinho.")
                st.rerun()
