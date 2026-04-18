import streamlit as st


st.title(" Boa tarde")
nome=st.text_input("Digite seu nome:")
if nome:
    st.write(f'Ola , {nome}')