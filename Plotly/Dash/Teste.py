import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import numpy as np

dados = pd.read_csv(r"C:\Users\chris\OneDrive\Documentos\Christian\Faculdade\IC\Projeto_Fluxo_VacinacaoSP\Dados\Dados_IBGE.csv")

app = dash.Dash()


app.layout = html.Div = (
    html.H1(children="Teste Dashboard dados IBGE", style={'textAlign': 'center', 'color':'#1C1C1C'}),
    html.Hr(),
    html.Div(id="cabecalho"),
    dcc.Dropdown(id='year-picker', options=dados['Municipio'], value=dados['Municipio'].unique().min),
    html.Hr(),
    #Footer
    html.Footer(html.H4(children="Feito por Christian Freitas", style={'textAlign': 'center'}))

)


if __name__ == '__main__':
    app.run_server()