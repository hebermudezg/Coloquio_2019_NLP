# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

# 
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Text Analysis UN"

# Aqui esta la magia **********************************
app.layout = html.Div(children=[
    html.H1(children='Gráficos Descriptivos'),
    html.Div(children='''
        Podrás seleccionar los gráficos descriptivos para el texto
    '''),

    dcc.Input(
        id='input_texto_1',
        value='Escriba su texto',
        type='text',
        style={'height':500, 'width': 1000 })

])




if __name__ == '__main__':
    app.run_server(debug=True)