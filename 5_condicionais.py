# verificando a media.
# solicite ao usuário a media do aluno.
# se maior ou igual a 7, mostre como aprovado.
# caso contrário, mostre como reprovado.

import streamlit as st 

st.title("Verificando a media")

média = st.number_input("Digite a media: ")

if st.button("Verificar"): 
    if média >=7: 
        st.success("aprovado")
    else:
        st.error("reprovado")

else: 
    st.info("informe a media")  

