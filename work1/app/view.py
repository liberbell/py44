import dash
from dash import callback, html, dcc, Input, Output, State
import plotly.graph_objects as go
import pandas as pd
import datetime
from assets.models import Data
from assets.database import db_session


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = db_session.query(Data.date, Data.subscribers, Data.reviews).all()
dates = []
subscribers = []
reviews = []
for datam in data:
    dates.append(datam.date)
    subscribers.append(datam.subscribers)
    reviews.append(datam.reviews)

diff_of_students = pd.Series(subscribers).diff().values
diff_of_reviewers = pd.Series(reviews).diff().values

app.layout = html.Div(children=[
    html.H2(children="Web application with Python"),
    html.Div(children=[
        dcc.Graph(
            id="subscribers_graph",
            figure={
                "data": [
                    go.Scatter(
                        x=dates,
                        y=subscribers,
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
                    title="Subscriber sum",
                    xaxis=dict(title="Date"),
                    yaxis=dict(title="Subscribers", side="left",
                                showgrid=False, range=[2500, max(subscribers)+100]),
                    yaxis2=dict(title="Subscriber diff", side="right", overlaying="y",
                                showgrid=False, range=[0, max(diff_of_students[1:])]),
                    margin=dict(l=200, r=200, b=100, t=100)

                )
            },
        ),
    dcc.Graph(
            id="reviewers_graph",
            figure={
                "data": [
                    go.Scatter(
                        x=dates,
                        y=reviews,
                        mode="lines+markers",
                        name="Reviewers Sum",
                        opacity=0.7,
                        yaxis="y1"
                    ),
                    go.Bar(
                        x=dates,
                        y=diff_of_reviewers,
                        name="Reviewers diff",
                        yaxis="y2"
                    )
                ],
                "layout": go.Layout(
                    title = "Reviewer sum",
                    xaxis = dict(title="Date"),
                    yaxis = dict(title="Subscribers", side="left",
                                 showgrid=False, range=[100, max(reviews)+100]),
                    yaxis2 = dict(title="Subscriber diff", side="right", overlaying="y",
                                 showgrid=False, range=[0, max(diff_of_reviewers[1:])]),
                    margin=dict(l=200, r=200, b=100, t=100)
                )
            },
        )
    ])
],
style={
    "textAlign": "center",
    "width": "1200px",
    "margin": "0 auto"
})

if __name__ == '__main__':
    app.run_server(debug=True)