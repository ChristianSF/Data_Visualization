import plotly.offline as pyo
import plotly.graph_objects as go
from plotly import subplots
import pandas as pd

dados = pd.read_csv(r'C:\Users\chris\OneDrive\Documentos\Christian\Programacao\_DataScience\Plotly\Data\2010SantaBarbaraCA.csv')
dados1 = pd.read_csv(r'C:\Users\chris\OneDrive\Documentos\Christian\Programacao\_DataScience\Plotly\Data\2010YumaAZ.csv')
dados2 = pd.read_csv(r'C:\Users\chris\OneDrive\Documentos\Christian\Programacao\_DataScience\Plotly\Data\2010SitkaAK.csv')

trace1 = go.Heatmap(x=dados['DAY'], y=dados['LST_TIME'],
                    z=dados['T_HR_AVG'], colorscale='Jet',
                    zmin=5, zmax=40)

trace2 = go.Heatmap(x=dados1['DAY'], y=dados1['LST_TIME'],
                    z=dados1['T_HR_AVG'],
                    zmin=5, zmax=40)

trace3 = go.Heatmap(x=dados2['DAY'], y=dados2['LST_TIME'],
                    z=dados2['T_HR_AVG'], colorscale='Jet',
                    zmin=5, zmax=40)

fig = subplots.make_subplots(rows=1, cols=3,
                          subplot_titles=['Sika AK', 'SB CA', 'Yuma'],
                          shared_yaxes=True)

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 1, 3)

pyo.plot(fig)


