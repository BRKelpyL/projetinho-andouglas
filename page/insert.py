import streamlit as st

import controller.users as users

def inserir():
    st.title('Inserir Dados')
    
    with st.form(key='insert'):
        input_name = st.text_input(label='Insira o nome')
        input_matricula = st.text_input(label='Insira a matrícula')
        input_senha = st.text_input(label='Insira a senha')
        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            users.incluir(input_name, input_matricula, input_senha)
            st.success('Cliente incluido com sucesso')