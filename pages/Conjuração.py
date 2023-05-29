import streamlit as st
import math
import time

st.set_page_config(
  page_title='RagCalc - Conjuração',
  page_icon=':bar_chart:',
  layout='wide',
  initial_sidebar_state='collapsed'
)

with open('css/style.css') as f:
  st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

ct = st.columns(1)
col1, col2 = st.columns(2)
cl1, cl2, cl3 = st.columns(3)

with st.container():
  with st.container():
      with col1:
          st.title('Conjuração Variável')
          st.write('Preencha abaixo os dados para obter o tempo de conjuração variável que a habilidade irá ficar após a redução por equipamentos e atributos.')
          tempo_conj_var = st.number_input('Tempo da Conjuração Variável (s)', min_value = 0.00, max_value = 100.00, value = 1.00, step = 0.01)
          reducao_conj_var_perc = st.number_input('Redução de Conjuração Variável por Equipamentos (%)', min_value = 0.00, max_value = 100.00, value = 0.00, step = 0.01)
          atr_dex = st.number_input('Destreza (Base + Bônus)', min_value = 1, max_value = 500, value = 100, step = 1)
          atr_int = st.number_input('Inteligência (Base + Bônus)', min_value = 1, max_value = 500, value = 100, step = 1)
          with st.spinner('Wait for it...'):
              conj_var = round(tempo_conj_var * (1 - math.sqrt((atr_dex * 2 + atr_int) / 530)) * (1 - reducao_conj_var_perc / 100), 4)
              if conj_var < 0.0000:
                  conj_var = 0.0000

      with col2:
          st.title('Conjuração Fixa')
          st.write('Preencha abaixo os dados para obter o tempo de conjuração fixa que a habilidade irá ficar após a redução por equipamentos e atributos.')
          tempo_conj_fixa = st.number_input('Tempo da Conjuração Fixa (s)', min_value = 0.00, max_value = 100.00, value = 1.00, step = 0.01)
          reducao_conj_fixa_perc = st.number_input('Redução de Conjuração Fixa por Equipamentos e Cartas (maior %)', min_value = 0.00, max_value = 100.00, value = 0.00, step = 0.01)
          reducao_conj_fixa_valor = st.number_input('Redução de Conjuração Fixa por Equipamentos e Cartas (s)', min_value = 0.00, max_value = 100.00, value = 0.00, step = 0.01)

          with st.spinner('Wait for it...'):
              conj_fixa = round((tempo_conj_fixa - reducao_conj_fixa_valor) * (1 - reducao_conj_fixa_perc / 100), 4)
              if conj_fixa < 0.0000:
                  conj_fixa = 0.0000

  with st.container():
      with cl1:
          st.title('')    
      with cl2:
          st.title('Conjuração Total')
          st.write('Tempo de Conjuração Variável (s)')
          st.write(conj_var)
          st.write('Tempo de Conjuração Fixa (s)')
          st.write(conj_fixa)
          st.write('Tempo de Conjuração (s)')
          st.write(conj_var + conj_fixa)
      with cl3:
          st.title('')
        
with st.container():
  with st.container():
      with col1:
          st.title('Conjuração Variável')
          st.write('Preencha abaixo os dados para obter o tempo de conjuração variável que a habilidade irá ficar após a redução por equipamentos e atributos.')
          tempo_conj_var1 = st.number_input('Tempo da Conjuração Variável 1(s)', min_value = 0.00, max_value = 100.00, value = 1.00, step = 0.01)
          reducao_conj_var_perc1 = st.number_input('Redução de Con11juração Variável por Equipamentos (%)', min_value = 0.00, max_value = 100.00, value = 0.00, step = 0.01)
          atr_dex1 = st.number_input('Destreza (Base11 + Bônus)', min_value = 1, max_value = 500, value = 100, step = 1)
          atr_int1 = st.number_input('Inteligência (11Base + Bônus)', min_value = 1, max_value = 500, value = 100, step = 1)
          with st.spinner('Wait for it...'):
              conj_var1 = round(tempo_conj_var * (1 - math.sqrt((atr_dex * 2 + atr_int) / 530)) * (1 - reducao_conj_var_perc / 100), 4)
              if conj_var1 < 0.0000:
                  conj_var1 = 0.0000

      with col2:
          st.title('Conjuração Fixa')
          st.write('Preencha abaixo os dados para obter o tempo de conjuração fixa que a habilidade irá ficar após a redução por equipamentos e atributos.')
          tempo_conj_fixa1 = st.number_input('Tempo da 11Conjuração Fixa (s)', min_value = 0.00, max_value = 100.00, value = 1.00, step = 0.01)
          reducao_conj_fixa_perc1 = st.number_input('Redu11ção de Conjuração Fixa por Equipamentos e Cartas (maior %)', min_value = 0.00, max_value = 100.00, value = 0.00, step = 0.01)
          reducao_conj_fixa_valor1 = st.number_input('Reduç111ão de Conjuração Fixa por Equipamentos e Cartas (s)', min_value = 0.00, max_value = 100.00, value = 0.00, step = 0.01)

          with st.spinner('Wait for it...'):
              conj_fixa1 = round((tempo_conj_fixa - reducao_conj_fixa_valor) * (1 - reducao_conj_fixa_perc / 100), 4)
              if conj_fixa1 < 0.0000:
                  conj_fixa1 = 0.0000
