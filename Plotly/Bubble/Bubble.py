import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

dados = pd.read_csv(r'C:\Users\chris\OneDrive\Documentos\Christian\Programacao\_DataScience\Plotly\Data\mpg.csv')

#print(dados.head())

data = [go.Scatter(x=dados['horsepower'],
                   y =dados['mpg'],
                   text=dados['name'],
                   mode='markers',
                   marker= dict(size=dados['weight']/100,
                                color=dados['cylinders'],
                                showscale=True))]




layout = go.Layout(title='Gráfico Bubble', hovermode='closest')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)