import streamlit as st
import numpy as np
import pandas as pd

st.title('Testando algumas funcionalidades com Streamlit')

st.write("Mostrando números aleatórios")
df = pd.DataFrame(
     np.random.randn(50, 20),
     columns=('col %d' % i for i in range(20)))
st.dataframe(df)

st.write("Primeiro Gráfico")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.area_chart(chart_data)

st.write("Primeiro Mapa com Streamlit")
map_data = pd.DataFrame({
    'awesome cities' : ['São Paulo', 'Itapecerica da Serra', 'Campinas', 'São José dos Campos'],
    'lat' : [-23.5489, -23.7175, -22.9064, -23.1791],
    'lon' : [-46.6388, -46.8496, -47.0616, -45.8872]
})
st.map(map_data)