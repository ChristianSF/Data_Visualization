import dash
import dash_core_components as dcc
import dash_html_components as html

markdown_teste = '''
#Dashboard e Markdown

testes testando o teste.
isso aqui funciona mesmo
'''


app = dash.Dash()

app.layout = html.Div([
    html.Label('Teste Markdown'),
    dcc.Markdown('''
        #Dashboard e Markdown
            ##testes testando o teste.
                ###isso aqui funciona mesmo
    '''),

    html.P(html.Label('Dropdown')),
    dcc.Dropdown(options=[{'label':'São Paulo',
                           'value':'SP'},
                          {'label':'Rio de Janeiro',
                           'value':'RJ'}],
                 value='SF'),
        html.P(html.Label('Slider')),
        dcc.Slider(min=-10, max=10, step=0.5, value=0,
                   marks={i: i for i in range(-10,10)}),

    html.P(html.Label('Some Radio Items')),
    dcc.RadioItems(options=[{'label':'São Paulo',
                           'value':'SP'},
                          {'label':'Rio de Janeiro',
                           'value':'RJ'}],
                   value='SF')
])



if __name__ == '__main__':
    app.run_server()