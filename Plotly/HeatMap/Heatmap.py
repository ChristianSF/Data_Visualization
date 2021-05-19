import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

dados = pd.read_csv(r'C:\Users\chris\OneDrive\Documentos\Christian\Programacao\_DataScience\Plotly\Data\2010SantaBarbaraCA.csv')

data = [go.Heatmap(x=dados['DAY'], y=dados['LST_TIME'],
                   z=dados['T_HR_AVG'].values.tolist(), colorscale='Jet')]

layout = go.Layout(title="Heatmap")

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)