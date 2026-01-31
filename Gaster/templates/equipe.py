import streamlit as st
from view import View
import pandas as pd
import time


class EquipeUI:
    def main():
        st.header("Equipe")
        tab1, = st.tabs(["Listar Funcionários"])
        with tab1: EquipeUI.equipar()

    def equipar():
        EquipeUI.listar()

    def listar():
        funcionario = View.equipe_listar()
        if len(funcionario) == 0: st.write("Nenhum funcionário cadastrado")
        else:
            list_dic = []
            for obj in funcionario: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "nome"])
