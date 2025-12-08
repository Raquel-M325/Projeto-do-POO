import streamlit as st
from view import View
import pandas as pd

class ConfirmarCarrinhoUI:

    def main(): #falta fazer com que o terminal mostre no site e não separado
        st.header("Confirmação de Compra")

        # Limita as opções entre 1 e 4, apenas inteiros
        pagar = int(st.number_input("Informe a opção de pagamento (1-Crédito, 2-Débito, 3-Pix, 4-Carrinho não finalizado):", min_value=1, max_value=4, step=1))

        if st.button("Confirmar"):
            # Aqui usamos diretamente o valor digitado
            if pagar == 1:
                View.pagamento_credito(numero_cartao, validade, CVV, nome)
                numero_cartao = input('Digite o número do seu cartão: ')
                validade = input('Digite a validade do cartão [MM/AA]: ')
                CVV = input('Digite o código de segurança (CVV): ')
                nome = input('Nome titular completo: ')

                st.success("Carrinho confirmado! Compra com sucesso!")
                st.rerun()


            elif pagar == 2:
                View.pagamento_debito(numero_cartao, validade, CVV, nome, banco, tipo)
                View.finalizacao()
                st.success("Carrinho confirmado! Compra com sucesso!")
                numero_cartao = input('Digite o número do seu cartão: ')
                validade = input('Digite a validade do cartão [MM/AA]: ')
                CVV = input('Digite o código de segurança (CVV): ')
                nome = input('Nome titular completo: ')
                banco = input('Digite qual é o banco: ')
                tipo = input('Que tipo de conta (corrente ou poupança): ')

                st.success("Carrinho confirmado! Compra com sucesso!")
                st.rerun()


            elif pagar == 3:
                View.pagamento_pix(nome, chave)
                nome = input('Nome titular completo: ')
                chave = input('Digite sua chave: ')

                st.success("Carrinho confirmado! Compra com sucesso!")
                st.rerun()


            elif pagar == 4:
                st.error("Compra não foi executada. Ainda há produtos no carrinho.")

            else:
                st.error("Opção de pagamento inválida.")

