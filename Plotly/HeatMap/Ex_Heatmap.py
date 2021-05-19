import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

dados = pd.read_csv(r'C:\Users\chris\OneDrive\Documentos\Christian\Programacao\_DataScience\Plotly\Data\flights.csv')

data = [go.Heatmap(x=dados['year'], y=dados['month'], z=dados['passengers'])]

layout = go.Layout(title='flights')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)

