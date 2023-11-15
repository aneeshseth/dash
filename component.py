from dash import Dash, html, dash_table
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

def generateGraph(dataframe, maxRows):
    return dash_table.DataTable(data=dataframe.to_dict('records'), page_size=maxRows)


app.layout = html.Div(children=[
    html.H1(children="Hello world"),
    html.Br(),
    generateGraph(df, 10)
])

if __name__ == '__main__':
    app.run(debug=True)