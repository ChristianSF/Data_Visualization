import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

dados = pd.read_csv(r'C:\Users\chris\OneDrive\Documentos\Christian\Programacao\_DataScience\Plotly\Data\mpg.csv')

data = [go.Histogram(x=dados['mpg'], xbins=dict(start=0,end=25, size=2))]

layout = go.Layout(title='Histograma')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)