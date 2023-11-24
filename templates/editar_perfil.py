import streamlit as st
from views import View
from models.cliente import Cliente,NCliente
import time

class EditarPerfil:
        def main():
             st.header("Edite os dados do seu perfil")
             EditarPerfil.mudar_dados()
        def mudar_dados():
            clientes = View.cliente_listar()
            if st.session_state["cliente_id"] == clientes[0].get_id():
                id = st.session_state["cliente_id"]
                email = st.text_input("Informe o novo e-mail")
                fone = st.text_input("Informe o novo fone")
                senha = st.text_input("Informe a nova senha")
                if st.button("Mudar dados"):
                    View.editar_perfil(id, "Admin", email, fone, senha)
                    st.success("Dados do Admin atualizados com sucesso")
                    time.sleep(2)
                    st.rerun()
            else:
                id = st.session_state["cliente_id"]
                nome = st.text_input("Informe o novo nome")
                email = st.text_input("Informe o novo e-mail")
                fone = st.text_input("Informe o novo fone")
                senha = st.text_input("Informe a nova senha")
                if st.button("Mudar dados"):
                    View.editar_perfil(id, nome, email, fone, senha)
                    st.success("Dados do Cliente atualizados com sucesso")
                    time.sleep(2)
                    st.rerun()