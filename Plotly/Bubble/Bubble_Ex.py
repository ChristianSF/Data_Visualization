import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

dados = pd.read_csv(r'C:\Users\chris\OneDrive\Documentos\Christian\Programacao\_DataScience\Plotly\Data\mpg.csv')

data = [go.Scatter(x=dados['displacement'],
                   y=dados['acceleration'],
                   text=dados['name'],
                   mode='markers',
                   marker=dict(size=dados['weight']/200))]

layout = go.Layout(hovermode='closest', title="Gráfico de bolhas")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
