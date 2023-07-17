import streamlit as st

import controller.users as users


def consultar():
    st.title('Consultar Dados')
    colunas = st.columns((1,2))
    campos = ['Matricula', 'Nome']
    
    for coluna, campo in zip(colunas, campos):
        coluna.write(campo)
    
    for item in users.selecionar():
        col1, col2 = st.columns((1,2))
        
        col1.write(item[0])
        col2.write(item[1])