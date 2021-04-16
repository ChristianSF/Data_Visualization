import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np

app = dash.Dash()

colors = {'background':'#FFFAFA', 'text':'#1C1C1C'}

#Criando dados
np.random.seed(50)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

app.layout = html.Div([dcc.Graph(id='scatterplot',
                                 figure= {'data':
                                        [go.Scatter(x=random_x,
                                                    y=random_y,
                                                    mode='markers',
                                                    marker = {
                                                        'size':12,
                                                        'color': 'rgb(51,204,153)',
                                                        'symbol':'pentagon',
                                                        'line':{'width':2}})],
                                 'layout':go.Layout(title='Gráfico de Dispersão',
                                                    xaxis={'title':'Eixo X'},
                                                    yaxis={'title':'Eixo Y'})}
                                 ),
                        dcc.Graph(id='scatterplot2',
                                 figure= {'data':
                                        [go.Scatter(x=random_x,
                                                    y=random_y,
                                                    mode='markers',
                                                    marker = {
                                                        'size':12,
                                                        'color': 'rgb(201,204,53)',
                                                        'symbol':'pentagon',
                                                        'line':{'width':2}})],
                                 'layout':go.Layout(title='Gráfico de Dispersão 2',
                                                    xaxis={'title':'Eixo X'},
                                                    yaxis={'title':'Eixo Y'})}
                                 ),
                        dcc.Graph(id='example', figure={'data':[
                            {'x':[1,2,3], 'y':[4,1,2], 'type':'bar', 'name':'Aids'},
                            {'x':[1, 2, 3], 'y':[2, 4, 5], 'type':'bar', 'name':'Diarréia'}],
                                    'layout':{
                                        'plot_bgcolor':colors['background'],
                                        'paper_bgcolor':colors['background'],
                                        'font':{'color':colors['text']},
                                        'title':'Gráfico de Barras'
                                    }})
                       ])

if __name__ == '__main__':
    app.run_server()