import sqlite3
import streamlit as st

if 'login' not in st.session_state:
    st.session_state['login'] = 'logado'

if st.session_state['login'] == 'nao_logado':
    with st.form("my_form"):
        usuario = st.text_input(label = "usuario")
        senha = st.text_input(label = "senha", type = "password")

        # Every form must have a submit button.
        resposta_login = st.form_submit_button("Submit")

        if resposta_login == True:
            con = sqlite3.connect("tutorial.db")
            cur = con.cursor()
            res = cur.execute("SELECT * FROM login WHERE usuario = '" + usuario + "' AND senha = '" + senha + "'")
            res = res.fetchall()

            if len(res) == 1:
                st.session_state['login'] = 'logado'
                st.experimental_rerun()
    
else:
    if st.button("Logoff"):
        st.session_state['login'] = 'nao_logado'
        st.experimental_rerun()