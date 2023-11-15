from dash import Dash, dcc, dash_table, html
import pandas as pd
import plotly.express as px

app = Dash(__name__)


df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')


def generateGraph(dataframe):
    return px.scatter(data_frame=dataframe, x="country", y="continent", hover_name="country")

app.layout = html.Div(children=[
    html.H1(children='Welcome to this page', id='h1-tag'),
    dcc.Graph(
        figure=generateGraph(df)
    )
])

if __name__ == '__main__':
    app.run(debug=True)