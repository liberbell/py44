import dash
from dash import callback, html, dcc, Input, Output, State
import plotly.graph_objects as go
import pandas as pd
import datetime


df = pd.read_csv("app/data.csv")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

dates = []
for _date in df["date"]:
    date = datetime.datetime.strptime(_date, "%Y/%m/%d").date()
    dates.append(date)

num_of_students = df["subscribers"].values
num_of_reviewers = df["reviews"].values

diff_of_students = df["subscribers"].diff().values
diff_of_reviewers = df["reviews"].diff().values

app.layout = html.Div(children=[
    html.H2(children="Web application with Python"),
    html.Div(children=[
        dcc.Graph(
            id="subscribers_graph",
            figure={
                "data": [
                    go.Scatter(
                        x=dates,
                        y=num_of_students,
                        mode="lines+markers",
                        name="Subscribers Sum",
                        opacity=0.7,
                        yaxis="y1"
                    )
                ]
            }
        )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)