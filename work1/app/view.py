import dash
from dash import callback, html, dcc, Input, Output, State
import plotly.graph_objects as go
import pandas as pd
import datetime


df = pd.read_csv("assets/data.csv")

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

print(diff_of_students)

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
                    ),
                    go.Bar(
                        x=dates,
                        y=diff_of_students,
                        name="Subscribers diff",
                        yaxis="y2"
                    )
                ],
                "layout": go.Layout(
                    title = "Subscriber sum",
                    xaxis = dict(title="Date"),
                    yaxis = dict(title="Subscribers", side="left",
                                 showgrid=False, range=[2500, max(num_of_students)+100]),
                    yaxis2 = dict(title="Subscriber diff", side="right", overlaying="y",
                                 showgrid=False, range=[0, max(diff_of_students[1:])]),

                )
            }
        )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)