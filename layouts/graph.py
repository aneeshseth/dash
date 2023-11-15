from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig = px.scatter(df, x="population", y="continent")

def getFigure(figu):
    return dcc.Graph(figure=figu)

app.layout = html.Div(children=[
    html.H1(children="hello world"),
    html.Br(),
    getFigure(fig)
])

if __name__ == '__main__':
    app.run(debug=True)