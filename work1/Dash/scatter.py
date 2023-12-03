import dash
from dash import callback, html, dcc, Input, Output, State
import numpy as np
import plotly.graph_objects as go

x1 = np.random.randint(0, 100, 50)
y1 = np.random.randint(0, 100, 50)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



if __name__ == '__main__':
    app.run_server(debug=True)