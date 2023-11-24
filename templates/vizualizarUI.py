import streamlit as st
import pandas as pd
from views import View
import time
import datetime

class VizualizarUI:
    def main():
        st.header("Agenda de Hoje")
        VizualizarUI.agendados()

    def agendados():
        horarios = View.agenda_listar()
        agendados_do_cliente = []
        for obj in horarios:
            if obj.get_id_cliente() == st.session_state["cliente_id"]:
                agendados_do_cliente.append(obj.to_json())
        df = pd.DataFrame(agendados_do_cliente)
        st.dataframe(df)




