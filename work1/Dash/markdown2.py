import dash
from dash import callback, html, dcc, Input, Output, State


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label("Dropdown"),
    dcc.Dropdown(
        options=[
            {"label": "Bob", "value": "bob"},
            {"label": "Eric", "value": "eric"},
            {"label": "Alex", "value": "alex"},
        ],
        value="eric"
    ),
    html.Label("Multi select dropdown"),
    dcc.Dropdown(
        options=[
            {"label": "Bob", "value": "bob"},
            {"label": "Eric", "value": "eric"},
            {"label": "Alex", "value": "alex"},
        ],
        value=["eric", "alex"],
        multi=True
    ),
    html.Label("Radio items"),
    dcc.RadioItems(
        options=[
            {"label": "Bob", "value": "bob"},
            {"label": "Eric", "value": "eric"},
            {"label": "Alex", "value": "alex"},
        ],
        value="eric"
    ),
    html.Label("Check boxes"),
    dcc.Checklist(
        options=[
            {"label": "Bob", "value": "bob"},
            {"label": "Eric", "value": "eric"},
            {"label": "Alex", "value": "alex"},
        ],
        value=["eric", "alex"]
    ),
    html.Label("Text input"),
    dcc.Input(value="Bob", type="text")
])

if __name__ == '__main__':
    app.run_server(debug=True)