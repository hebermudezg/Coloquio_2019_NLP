
import dash
import dash_core_components as dcc


app = dash.Dash(__name__)
dcc.Slider(value=4, min=-10, max=20, step=0.5,
           labels={-5: '-5 Degrees', 0: '0', 10: '10 Degrees'})



if __name__ == '__main__':
    app.run_server(debug=True)