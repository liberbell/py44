import dash
from dash import callback, html, dcc, Input, Output, State


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Markdown("""
# Title 1
## Title 2

- sub title
- sub title
- sub title
""")
])

if __name__ == '__main__':
    app.run_server(debug=True)