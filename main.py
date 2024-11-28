import streamlit as st
import numpy as np
import pandas as pd

col1, col2, col3, col4 = st.columns(4)
st.sidebar.title("Menu")



pagselect = st.sidebar.selectbox('Select a página: ', ['Vendas', 'Cadastro', 'Contagem'])

if pagselect == 'Vendas':
    
    st.write("""
            # Dashboard de vendas
            """)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("Líquida")


    with col2:
        st.write("Mercearia")


    with col3:
        st.write("Higiêne")


    with col4:
        st.write("Sorveteria")



elif pagselect == 'Cadastro':
    
    st.write("""
                # Formulário de Cadastro
            """)
    col1, col2 = st.columns(2)
    with col1:
        st.write("Líquida")


    with col2:
        st.write("Mercearia")


else: 
    st.write("""
                # Dashboard de Contagem
            """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Líquida")
        data1 = (1,4,2,5,7)
        st.line_chart(data1)

    with col2:
        st.write("Mercearia")
        data1 = (1,4,2,5,7)
        st.scatter_chart(data1)

    with col3:
        st.write("Higiêne")
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        st.bar_chart(chart_data)


    st.write("Higiêne")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)
