import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

dados = pd.read_csv(r'C:\Users\chris\OneDrive\Documentos\Christian\Programacao\_DataScience\Plotly\Data\abalone.csv')

data = [go.Histogram(x=dados['length'], xbins=dict(start=0, end=1, size=0.02))]

layout = go.Layout(title="Meu histograma")

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)