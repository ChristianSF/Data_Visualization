import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import base64

dados = pd.read_csv("../Data/wheels.csv")

app = dash.Dash()

def encode_image(image_file):
    encode = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encode.decode())


app.layout = html.Div([
            dcc.RadioItems(id='wheels',
                           options=[{'label':i,'value':i} for i in dados['wheels'].unique()],
                            value=1),
            html.Div(id='wheels-output'),
            html.Hr(),
            dcc.RadioItems(id='colors', options=[{'label':i,'value':i} for i in dados['color'].unique()],
                            value='blue'),
            html.Div(id='colors-output'),
            html.Img(id='display-image', src='children', height=300)

], style={'fontFamily':'helvetica', 'fontSize':18})


@app.callback(Output('wheels-output', 'children'),
              [Input('wheels', 'value')])
def callback_a(wheels_value):
    return "Você escolhe {}".format(wheels_value)

@app.callback(Output('colors-output', 'children'),
              [Input('colors','value')])
def callback_b(colors_value):
    return  "Você escolhe {}".format(colors_value)

@app.callback(Output('display-image', 'src'),[Input('wheels', 'value'),
                                             Input('colors','value')])
def callback_image(wheel, color):
    path = '../data/Images/'

    return encode_image(path+dados[(dados['wheels']==wheel) & (dados['color'] ==color)]['image'].values[0])


if __name__ == '__main__':
    app.run_server()