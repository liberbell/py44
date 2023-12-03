import dash
from dash import callback, html, dcc, Input, Output, State
# import dash_core_components as dcc
# import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    "background": "black",
    "text": "white",
}

app.layout = html.Div(children=[
    html.H1(
        children='Hello Dash',
        style={
            "textAlign": "center",
            "color": colors["text"]
        }
    ),

    html.Div(
        children='''
        Dash: A web application framework for Python.
    ''',
    style={
            "textAlign": "center",
            "color": colors["text"]
    }
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 6], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [9, 4, 5], 'type': 'bar', 'name': 'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)