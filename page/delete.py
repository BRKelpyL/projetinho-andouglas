import streamlit as st

import controller.users as users

def deletar():
    st.title('Deletar Dados')
    
    with st.form(key='delete'):
        input_matricula = st.text_input(label='Insira a matrícula')
        
        buttom_delete = st.form_submit_button('Deletar')
        
        if buttom_delete:
            users.deletar(input_matricula)
            st.success('Cliente excluido com sucesso')