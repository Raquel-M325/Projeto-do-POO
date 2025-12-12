import streamlit as st
from view import View
import time
import pandas as pd

class ManterCategoriaUI:
    def main():
        st.header("Cadastro de Categorias")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterCategoriaUI.listar()
        with tab2: ManterCategoriaUI.inserir()
        with tab3: ManterCategoriaUI.atualizar()
        with tab4: ManterCategoriaUI.excluir()


    def listar():
        categoria = View.categoria_listar()
        if len(categoria) == 0: st.write("Nenhuma categoria adicionado")
        else:
            list_dic = []
            for obj in categoria: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "descricao"])        


    def inserir():
        descricao = st.text_input("Informe a descrição")
        if st.button("Inserir"):
            try:
                View.categoria_inserir(descricao)
                st.success("Categoria inserido com sucesso")
            except ValueError:
                st.error("Descrição vazia") 
            
            except KeyError:
                st.error("Descrição repetida") 

            time.sleep(2)
            st.rerun()
        
    def atualizar():
        categoria = View.categoria_listar()
        if len(categoria) == 0: st.write("Nenhuma categoria cadastrado")
        else:
            op = st.selectbox("Atualização de Categorias", categoria)
            descricao = st.text_input("Informe a nova descrição", op.get_descricao())
            if st.button("Atualizar"):
                try:
                    id = op.get_id()
                    View.categoria_atualizar(id, descricao)
                    st.success("Categoria atualizado com sucesso")

                except ValueError:
                    st.error("Descrição vazia") 
            
                except KeyError:
                    st.error("Descrição repetida") 


                time.sleep(2)
                st.rerun()

    def excluir():
        categoria = View.categoria_listar()
        if len(categoria) == 0: st.write("Nenhum categoria cadastrado")
        else:
            op = st.selectbox("Exclusão de Categorias", categoria)
            if st.button("Excluir"):
                try:
                    id = op.get_id()
                    View.categoria_excluir(id)
                    st.success("Categoria excluído com sucesso")
                except: 
                    st.error("Existência de produto na categoria")
                time.sleep(2)
                st.rerun()