import streamlit as st
from view import View
import pandas as pd
import time

class ConfirmarCarrinhoUI:

    def main(): #falta fazer com que o terminal mostre no site e não separado
        st.header("Confirmação de Compra")
        tab1, = st.tabs(["Pagamento"])
        with tab1: ConfirmarCarrinhoUI.pagamento()


        
    def pagamento():   # Limita as opções entre 1 e 4, apenas inteiros
        pagar = st.number_input("Informe a opção de pagamento (1-Crédito, 2-Débito, 3-Pix)", min_value=0, max_value=3, step=0)
        if pagar == 1: pagamento = ConfirmarCarrinhoUI.pagamento_credito()
        if pagar == 2: pagamento = ConfirmarCarrinhoUI.pagamento_debito()
        if pagar == 3: pagamento = ConfirmarCarrinhoUI.pagamento_pix()
        if st.button("Confirmar"):
            View.comprar_carrinho(pagamento, st.session_state["cliente_id"])
            st.success("Carrinho confirmado! Compra com sucesso!")
            time.sleep(2)
            st.rerun()
            
    def pagamento_credito():                                # Aqui usamos diretamente o valor digitado
        numero_cartao = st.text_input('Digite o número do seu cartão: ')
        validade = st.text_input('Digite a validade do cartão [MM/AA]: ')
        CVV = st.text_input('Digite o código de segurança (CVV): ')
        nome = st.text_input('Nome titular completo: ')
        return "Crédito"


    def pagamento_debito():
        numero_cartao = st.text_input('Digite o número do seu cartão: ')
        validade = st.text_input('Digite a validade do cartão [MM/AA]: ')
        CVV = st.text_input('Digite o código de segurança (CVV): ')
        nome = st.text_input('Nome titular completo: ')
        banco = st.text_input('Digite qual é o banco: ')
        tipo = st.text_input('Que tipo de conta (corrente ou poupança): ')
        return "Débito"


    def pagamento_pix():
        nome = st.text_input('Nome titular completo: ')
        chave = st.text_input('Digite sua chave: ')
        return "Pix"

        # else:     COLOCAR NO EXCEPT
        #     st.error("Opção de pagamento inválida.")