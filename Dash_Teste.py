import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {'background':'#111111', 'text':'#7FDBFF'}
#colors['text']

app.layout = html.Div(children=[
    html.H1('Primeira Dashboard!', style={'textAlign':'center',
                                          'color':colors['text']}),
    html.Div('Dash: Dashboards Web com Python'),
    dcc.Graph(id='example', figure={'data':[
                            {'x':[1,2,3], 'y':[4,1,2], 'type':'bar', 'name':'Aids'},
                            {'x':[1, 2, 3], 'y':[2, 4, 5], 'type':'bar', 'name':'Diarréia'}],
                                    'layout':{
                                        'plot_bgcolor':colors['background'],
                                        'paper_bgcolor':colors['background'],
                                        'font':{'color':colors['text']},
                                        'title':'Gráfico de Barras'
                                    }})
], style={'backgroundColor':colors['background']}
),

if __name__ == '__main__':
    app.run_server(debug=True)