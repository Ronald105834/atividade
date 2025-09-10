import streamlit as st 

primeiro_numero = st.number_input("digite o primeiro numero:")
segundo_numero = st.number_input("digite o segundo numero:")

st.title("atividade")

media = ("primeiro_numero + segundo_numero")/2 
soma = ("primeiro_numero + segundo_numero")
produto = ("primeiro_numero * segundo_numero")
maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

if st.button("Verificar"):
    if primeiro_numero and segundo_numero:
        st.write(f"soma: {soma}")
        st.write(f"produto: {produto}")
        st.write(f"média: {media}")
        st.write(f"maior: {maior}")
        st.write(f"menor: {menor}")
else: 
    st.info("informe os numeros.")