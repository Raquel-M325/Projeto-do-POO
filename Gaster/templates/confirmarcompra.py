import streamlit as st
from view import View
import pandas as pd

class ConfirmarCarrinhoUI:
    def main():
        st.header("Confirmação de Compra")
        pagar = st.number_input("Informe a opção de pagamento:")

        if st.button("Confirmar"):
            verificacao = View.opcao_pagar(pagar)
            if verificacao is not None:
                if verificacao == 1:
                    credito = View.pagamento_credito()  
                
                if verificacao == 2:
                    debito = View.pagamento_debito()

                if verificacao == 3:
                    pix = View.pagamento_pix()

            finalizacao = View.finalizacao()
            st.session_state["usuario_id"] = finalizacao["id"] #acho que nessa parte esteja incompleta
            st.success("Carrinho confirmado! Compra com sucesso!")
            st.rerun()

        else:
            st.error("Compra não foi executada. Ainda há produtos no carrinho.")
            st.rerun()
