import streamlit as st
st.title('calculadora')
num1 = st.number_input('insira o primeiro número: ')
num2 = st.number_input('insira o segundo número: ')

if st.button('somar'):
    result = num1 + num2
    st.text('resultado: ')
    st.title(result)
    if st.button('voltar'):
      result = 0
elif st.button('subtrair'):
    result = num1 - num2
    st.text('resultado: ')
    st.title(result)
    if st.button('voltar'):
      result = 0
elif st.button('mult'):
    result = num1 * num2
    st.text('resultado: ')
    st.title(result)
    if st.button('voltar'):
      result = 0
elif st.button('divi'):
    result = num1 / num2
    st.text('resultado: ')
    st.title(result)
    if st.button('voltar'):
      result = 0
elif st.button('exponenciar'):
    result = num1 ** num2
    st.text('resultado: ')
    st.title(result)
    if st.button('voltar'):
      result = 0
elif st.button('raiz'):
    result = num1 ** (1/num2)
    st.text('resultado: ')
    st.title(result)
    if st.button('voltar'):
      result = 0
