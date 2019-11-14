import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly import tools
from plotly import graph_objs as go

fig = tools.make_subplots(rows=2, shared_xaxes=True)
fig.add_scatter(x=[1,2,3], y=[2,1,2])
fig.add_scatter(x=[1,2,3], y=[5,3,3], yaxis='y2')
fig.layout.xaxis.dtick=0.5

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[

dcc.Graph(
    id='graph1',
    figure = fig
),

dcc.Slider(
    id='temp-slider',
    min=0,
    max=10,
    step=0.2,
    value=0
)

])

@app.callback(
    Output('graph1','figure'), [Input('temp-slider','value')]
)

def update_graph(value): 
    fig.layout.xaxis.range = [value,value+1]
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)