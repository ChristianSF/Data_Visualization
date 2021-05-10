import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import plotly.offline as pyo
import pandas as pd
from datetime import datetime

dados = pd.read_csv(r"CSNA3.SA.csv")

max = dados['High'].max()
min = dados['High'].min()
media = dados['High'].mean()
media_movel = dados['High'].rolling(window=30, min_periods=1).mean()

'''
Cores:
#008F39
#831D1C
#FFBF00
'''

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])


fig = go.Figure(data=[go.Candlestick(x=dados['Date'],
                open=dados['Open'],
                high=dados['High'],
                low=dados['Low'],
                close=dados['Close'])])

fig.update_layout(title_text='Ações da Companhia Siderúrgica Nacional - CSN.3', xaxis_title="Data (2016 - 2021)",
    yaxis_title="Preço em R$", template="plotly_dark")


fig2 = px.line(dados, x=dados['Date'], y=dados['Open'], title='Abertura da Ação')
fig2.update_layout(xaxis_title="Data (2016 - 2021)", yaxis_title="Preço em R$", template="plotly_dark")

fig3 = px.line(dados, x=dados['Date'], y=dados['Close'], title='Fechamento da Ação')
fig3.update_layout(xaxis_title="Data (2016 - 2021)", yaxis_title="Preço em R$", template="plotly_dark")

fig4 = px.line(dados, x=dados['Date'], y=media_movel, title='Média móvel da Ação')
fig4.update_layout(xaxis_title="Data (2016 - 2021)", yaxis_title="Preço em R$", template="plotly_dark")



app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='teste', figure=fig)
                 ])
            ], inverse=True)
        ], width=9, align="start"),

            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Escolha o ano:", className="card-title", style={'color':'#FFFFFF'}),
                        dcc.Dropdown(
                            id='demo-dropdown',
                                options=[
                                    {'label': '2016', 'value': '16'},
                                    {'label': '2017', 'value': '17'},
                                    {'label': '2018', 'value': '18'},
                                    {'label': '2019', 'value': '19'},
                                    {'label': '2020', 'value': '20'},
                                    {'label': '2021', 'value': '21'}
                                ],
                            value='21')
                    ])
                ], className="mb-2"),
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Preço Máximo:", className="card-title"),
                        html.P("R$ {:.2f}".format(max), className="card-text", style={'color':'#008F39'}),
                    ])
                ], className='mb-2 mt-0', inverse=True),
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Preço Mínimo:", className="card-title"),
                        html.P("R$ {:.2f}".format(min), className="card-text", style={'color':'#831D1C'}),
                    ])
                ], className='mb-2', inverse=True),
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Preço Médio", className="card-title"),
                        html.P("R$ {:.2f}".format(media), className="card-text", style={'color':'#FFBF00'}),
                    ])
                ], inverse=True)
            ], width=3, align="end", className='mb-2 mt-0'),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='Grafico2', figure=fig2)
                ])
            ], className='mt-2')
        ], align="start"),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='Grafico3', figure=fig3)
                ])
            ], className='mt-2')
        ], align="center")
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("Feito por Christian Freitas"),
                ])
            ], inverse=True)
        ], align="center", className="mt-2 mb-1", style={'textAlign':'center'})
    ])

], fluid=True)


if __name__ == '__main__':
    app.run_server()