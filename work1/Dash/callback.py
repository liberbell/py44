import dash
from dash import callback, html, dcc, Input, Output, State


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id="input-div", value="Initial value", type="text"),
    html.Div(id="output-div")
])

@app.callback(
    Output(component_id="output-div", component_property="children"),
    [Input(component_id="input-div", component_property="value")]
)

def update(input_value):
    return "You entered: {}".format(input_value)

if __name__ == '__main__':
    app.run_server(debug=True)