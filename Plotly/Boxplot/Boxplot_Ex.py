import plotly.offline as pyo
import plotly.graph_objects as go
import numpy as np
import pandas as pd

dados = pd.read_csv(r'C:\Users\chris\OneDrive\Documentos\Christian\Programacao\_DataScience\Plotly\Data\abalone.csv')

a = np.random.choice(dados['rings'], 30, replace=False)
b = np.random.choice(dados['rings'], 20, replace=False)

data = [go.Box(y=a, name='A'),
        go.Box(y=b, name='B')]

layout = go.Layout(title="2 Boxplot com valores aleatórios")

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)

