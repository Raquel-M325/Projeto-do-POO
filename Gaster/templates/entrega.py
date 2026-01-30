import streamlit as st
import pandas as pd
from view import View
import time

class ReclameAquiUI:
    def main():
        st.header("Aba de Reclamações")
        tab1, tab2 = st.tabs(["Reclamar", "Listar Reclamações"])
        with tab1:ReclameAquiUI.reclamar()
        with tab2:ReclameAquiUI.reclamacoes()

        
    def reclamar():
        for obj in View.cliente_listar():
            if obj.get_id() == st.session_state["cliente_id"]:
                cliente = obj.get_id()
                break
        reclamacao = View.reclameaqui_listar()
        if len(reclamacao) == 0: st.write("Diga sua reclamação")
        else:
            insatisfacao = st.text_input("Diga-nos a sua insatisfação")
            if st.button("Reclamar"):
                try:
                    View.reclameaqui_inserir(insatisfacao, cliente)
                    st.success("Agradecemos pelo seu feedback")
                except ValueError:
                    st.error("Sua reclamação não foi aceita")
                time.sleep(2)
                st.rerun()
    def reclamacoes():
        reclamacoes = View.reclameaqui_listar()
        if len(reclamacoes) == 0: st.write("Nenhuma reclamação registrada")
        else:
            list_dic = []
            for obj in reclamacoes: 
                if obj.get_idCliente() == st.session_state["cliente_id"]:
                    list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["reclamacao","idCliente"])       

