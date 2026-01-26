import streamlit as st
from view import View

class LoginUI:
    def main():
        st.header("Entrar no sistema")
        email = st.text_input("Informe seu e-mail")
        senha = st.text_input("Informe sua senha", type="password")
        if st.button("Entrar"):
            c = View.cliente_autenticar(email, senha)
            if c == None:
                st.write("E-mail ou senha inválidos")
            else:
                st.session_state["cliente_id"] = c["id"]
                st.session_state["cliente_nome"] = c["nome"]
                st.rerun()
        if st.button("Esqueci a senha"):
            try:
                c = Viem.cliente_listar()
                if c == None: 
                    st.write("Não há clientes cadastrados")
                else:
                    emailn = st.text_input("Informe seu e-mail cadastrado")
                    for obj in View.cliente_listar():
                        if obj.get_email == emailn:
                            id = obj.get_id()
                            nome = obj.get_nome()
                            fone = obj.get_fone()
                            senhan = st.text_input("Informe sua nova senha", type="password")
                            cli = View.cliente_atualizar(id, nome, email, fone, senha)
                            st.session_state["cliente_id"] = c["id"]
                            st.session_state["cliente_nome"] = c["nome"]
                            st.rerun()
            except:
                st.error("Senha não autorizada")
                st.rerun()