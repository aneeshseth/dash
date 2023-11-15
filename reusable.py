from dash import Dash, dcc, html, dash_table
import pandas as pd
import plotly.express as px

app = Dash(__name__)

colors = {
    "text": "#00FF00"
}

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

def generateFig(dataframe, maxRows):
    return dash_table.DataTable(data=dataframe.to_dict('records'), page_size=maxRows)


app.layout = html.Div(children=[
    html.H1(children="Welcome to this page", style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.Br(),
    html.Br(),
    generateFig(df, 10)
])


if __name__ == '__main__':
    app.run(debug=True)