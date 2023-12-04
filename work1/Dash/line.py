import dash
from dash import callback, html, dcc, Input, Output, State
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("time_series.csv")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(
        id="sample-line",
        figure={
            "data":[
                go.Scatter(
                    x=df["date"],
                    y=df["MSFT"],
                    mode="lines",
                    opacity=0.7,
                    marker={
                        "size":15,
                    },
                    name="Microsoft",
                ),
                go.Scatter(
                    x=df["date"],
                    y=df["AAPL"],
                    mode="lines",
                    opacity=0.7,
                    marker={
                        "size":15,
                    },
                    name="Apple",
                )
            ],
            "layout": go.Layout(
                xaxis={"title": "X axis"},
                yaxis={"title": "Y axis"},
                width=1000,
                height=500,
            )
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)