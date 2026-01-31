import streamlit as st
from view import View
import pandas as pd
import time


class EquipeUI:
    def main():
        st.header("Equipe")
        tab1, tab2, tab3 = st.tabs(["Listar Funcionários", "Cadastrar um Funcionário", "Retirar um Funcionário"])
        with tab1:EquipeUI.equipar()
        with tab2:EquipeUI.equiparar()
        with tab3:EquipeUI.retirar()

    def equipar():
        EquipeUI.listar()

    def listar():
        funcionario = View.equipe_listar()
        if len(funcionario) == 0: st.write("Nenhum funcionário cadastrado")
        else:
            list_dic = []
            for obj in funcionario: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "nome", "funcao"])

    def equiparar():
        EquipeUI.cadastrar()


    def cadastrar():
        nome = st.text_input("Informe o nome do funcionário")
        funcionalidade =  st.text_input("Informe a função do funcionário")
        if st.button("Inserir"):
            try:
                View.equipe_inserir(nome, funcionalidade)
                st.success("equipe inserido com sucesso")
            except ValueError:
                st.error("Descrição vazia") 
            
            except KeyError:
                st.error("Descrição repetida") 

            time.sleep(2)
            st.rerun()
    

    def retirar():
        funcionario = View.equipe_listar()
        if len(funcionario) == 0: st.write("Nenhum funcionário cadastrado")
        else:
            list_dic = []
            for obj in funcionario: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "nome"])

        retirar = st.number_input("Digite o id da equipe para retirar o funcionário", value=0, step = 0)
        if st.button("retirado"):
            try:
                View.equipe_excluir(retirar)
                st.success("Funcionário retirado")
                time.sleep(2)
                st.rerun()
            except ValueError:
                st.error("Erro ao retirar")
                time.sleep(2)
                st.rerun()
