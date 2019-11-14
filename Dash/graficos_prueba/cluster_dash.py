import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import dash_bio as dashbio
##oja de estilos graficar *****************************************************************
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
##o *****************************************************************

df = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/clustergram_mtcars.tsv',
                 sep='	', skiprows=4).set_index('model')

columns = list(df.columns.values)
rows = list(df.index)

clustergram = dashbio.Clustergram(
    data=df.loc[rows].values,
    row_labels=rows,
    column_labels=columns,
    color_threshold={
        'row': 250,
        'col': 700
    },
    height=800,
    width=700,
    display_ratio=[0.1, 0.7]
)

app.layout = html.Div(children=[

  html.H1(
        children='Hello Dash'
    ),

  dcc.Graph(figure=clustergram)
])
    

if __name__ == '__main__':
    app.run_server(debug=True)
