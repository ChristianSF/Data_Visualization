import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd

dados = pd.read_csv("https://raw.githubusercontent.com/Pierian-Data/Plotly-Dashboards-with-Dash/master/Data/OldFaithful.csv")

app = dash.Dash()

app.layout = html.Div([dcc.Graph(id='old_faithful',
                                 figure={'data':[go.Scatter(x=dados['X'],
                                                            y=dados['Y'],
                                                            mode='markers')],
                                         'layout':go.Layout(title='Old Faithful Eruptions',
                                                            xaxis={'title':'Duration'},
                                                            yaxis={'title':'Interval'})})])

if __name__ == '__main__':
    app.run_server()