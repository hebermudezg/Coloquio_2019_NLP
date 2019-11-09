# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[

    ## *********************************** texto **********************************
    html.H1(children='Ingresa tu texto'),
    dcc.Textarea(
    id = 'input_texto_1',
    placeholder='Ingrese su texto',
    value='',
    style={'width': '100%'}
    ),  


    ## *********************************** Graficos **********************************
    html.H1(children='Análisis descriptivo'),
    dcc.Textarea(
    id = 'input_texto_2',
    placeholder='Ingrese su texto',
    value='',
    style={'width': '100%'}
    ),  


    ## *********************************** summarizer **********************************
    html.H1(children='Resumen'),
    dcc.Textarea(
    id = 'input_texto_3',
    placeholder='Ingrese su texto',
    value='',
    style={'width': '100%'}
    ),  

    
])




if __name__ == '__main__':
    app.run_server(debug=True)