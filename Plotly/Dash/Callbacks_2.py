import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

dados = pd.read_csv("https://raw.githubusercontent.com/Pierian-Data/Plotly-Dashboards-with-Dash/master/Data/gapminderDataFiveYear.csv")

#print(dados.head())

app = dash.Dash()

year_options = []
for year in dados['year'].unique():
    year_options.append({'label':str(year), 'value':year})

app.layout = html.Div([
        #Titulo
        html.H1(children="Teste Dashboard", style={'textAlign': 'center', 'color':'#1C1C1C'}),
        html.Hr(),
        #Dropdwon
        html.P(dcc.Dropdown(id='year-picker', options=year_options, value=dados['year'].min())),
        #Gráfico
        dcc.Graph(id='graph'),
        html.Hr(),
        #Footer
        html.Footer(html.H4(children="Feito por Christian Freitas", style={'textAlign': 'center'}))

])

@app.callback(Output('graph','figure'),
              [Input('year-picker', 'value')])
def update_figure(selected_year):
    dados_filtrados = dados[dados['year'] == selected_year]
    traces = []

    for nome_continente in dados_filtrados['continent'].unique():
        dados_continente = dados_filtrados[dados_filtrados['continent']==nome_continente]
        traces.append(go.Scatter(
            x = dados_continente['gdpPercap'],
            y = dados_continente['lifeExp'],
            mode = 'markers',
            opacity = 0.7,
            marker = {'size':15},
            name=nome_continente

        ))

    return {'data':traces,
            'layout':go.Layout(title='Meu Gráfico', xaxis={'title':'Eixo X', 'color':'#696969'}, yaxis={'title':'Eixo Y', 'color':'#696969'})}

if __name__ == '__main__':
    app.run_server()