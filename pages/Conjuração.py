import streamlit as st
import math
import time

st.set_page_config(
  page_title='RagCalc - Conjuração',
  page_icon=':bar_chart:',
  layout='wide',
  initial_sidebar_state='collapsed'
)

col1, col2 = st.columns(2)

with st.container():
    with col1:
        st.title('Conjuração Variável')
        st.write('Preencha abaixo os dados para obter o tempo de conjuração variável que a habilidade irá ficar após a redução por equipamentos e atributos.')
        tempo_conj_var = st.number_input('Tempo da Conjuração Variável (s)', min_value = 0.00, max_value = 100.00, value = 1.00, step = 0.01)
        reducao_conj_var_perc = st.number_input('Redução de Conjuração Variável por Equipamentos (%)', min_value = 0.00, max_value = 100.00, value = 0.00, step = 0.01)
        atr_dex = st.number_input('Destreza', min_value = 1, max_value = 500, value = 100, step = 1)
        atr_int = st.number_input('Inteligência', min_value = 1, max_value = 500, value = 100, step = 1)
        with st.spinner('Wait for it...'):
            conj_var = round(tempo_conj_var * (1 - math.sqrt((atr_dex * 2 + atr_int) / 530)) * (1 - reducao_conj_var_perc / 100), 4)
            time.sleep(1)
            if conj_var < 0.0000:
                conj_var = 0.0000

    with col2:
        st.title('Conjuração Fixa')
        st.write('Preencha abaixo os dados para obter o tempo de conjuração fixa que a habilidade irá ficar após a redução por equipamentos e atributos.')
        tempo_conj_fixa = st.number_input('Tempo da Conjuração Fixa (s)', min_value = 0.00, max_value = 100.00, value = 1.00, step = 0.01)
        reducao_conj_fixa_perc = st.number_input('Redução de Conjuração Fixa por Equipamentos e Cartas (%)', min_value = 0.00, max_value = 100.00, value = 0.00, step = 0.01)
        reducao_conj_fixa_valor = st.number_input('Redução de Conjuração Fixa por Equipamentos e Cartas (s)', min_value = 0.00, max_value = 100.00, value = 0.00, step = 0.01)
        
        with st.spinner('Wait for it...'):
            conj_fixa = round((tempo_conj_fixa - reducao_conj_fixa_valor) * (1 - reducao_conj_fixa_perc / 100), 4)
            time.sleep(1)
            if conj_fixa < 0.0000:
                conj_fixa = 0.0000

with st.container():
    st.title('Conjuração Total')
    st.write('Tempo de Conjuração Variável (s)')
    st.write(conj_var)
    st.write('Tempo de Conjuração Fixa (s)')
    st.write(conj_fixa)
    st.write('Tempo de Conjuração (s)')
    st.write(conj_var + conj_fixa)
