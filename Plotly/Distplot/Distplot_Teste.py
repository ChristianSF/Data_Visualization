import plotly.figure_factory as ff
import numpy as np

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) +2
x4 = np.random.randn(200) + 4

dados = [x1, x2, x3, x4]

grupo = ['Grupo 1', 'Grupo 2', 'Grupo 3', 'Grupo 4']

fig = ff.create_distplot(dados, grupo, bin_size=.2)
fig.show()