import streamlit as st
import pandas as pd
from views import View
import time
import datetime

class AgendarHorarioUI:
    def main():
        st.header("Agenda de Hoje")
        tab1, tab2 = st.tabs(["Agenda da semana", "Agendamento"])
        with tab1: AgendarHorarioUI.listar()
        with tab2: AgendarHorarioUI.agendar()

    def listar():
        agendas = View.agenda_listar_seguintes()
        if len(agendas) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in agendas: 
                dic.append(obj.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df)
    def agendar():
        horarios = View.agenda_listar_seguintes()
        horario = st.selectbox("Selecione um horário", horarios)
        servicos = View.servico_listar()
        servico = st.selectbox("Selecione um serviço", servicos)
        data = horario.get_data()
        id = st.session_state["cliente_id"]
        if st.button("Agendar"):
            View.agenda_atualizar(horario.get_id(), data,
            False, id, servico.get_id())
            st.success("Agendamento realizado com sucesso")
            time.sleep(2)
            st.rerun()
