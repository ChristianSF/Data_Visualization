import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

dados = pd.read_csv("https://raw.githubusercontent.com/Pierian-Data/Plotly-Dashboards-with-Dash/master/Data/mpg.csv")

app = dash.Dash()

features = dados.columns

app.layout = html.Div([
        html.Div([
            dcc.Dropdown(id='xaxis',
                         options=[{'label': i, 'value': i}
                                  for i in features], value='displacement')
        ], style={'width':'48%', 'display':'inline-block'}),
        html.Div([
            dcc.Dropdown(id='yaxis',
                         options=[{'label': i.title(), 'value': i}
                                  for i in features], value='acceleration')
        ], style={'width':'48%', 'display':'inline-block', 'float':'right'}),
        dcc.Graph(id='feature-graphic')

], style={'padding':10})


@app.callback(Output('feature-graphic', 'figure'),
              [Input('xaxis','value'),
               Input('yaxis', 'value')])
def update_grafico(xaxis_name, yaxis_name):
    return {'data':[go.Scatter(x=dados[xaxis_name],
                               y=dados[yaxis_name],
                               text=dados['name'],
                               mode='markers',
                               marker={'size':12, 'opacity':0.5, 'line':{'width':0.5, 'color':'white'}})],
            'layout':go.Layout(title='Minha Dashboard para MPG',
                                xaxis={'title':xaxis_name.title(), 'color':'#696969'},
                                yaxis={'title':yaxis_name.title(), 'color':'#696969'},
                                hovermode='closest')}

if __name__ == '__main__':
    app.run_server()