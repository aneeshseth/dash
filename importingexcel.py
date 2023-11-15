
from dash import Dash, html, dash_table
import pandas as pd


df = pd.read_excel('Book1.xlsx', sheet_name='Sheet1')


app = Dash(__name__)


app.layout = html.Div([
    html.Div(children='My First App with Data'),
    dash_table.DataTable(
        id='table',
        columns=[{'name': col, 'id': col} for col in df.columns],
        data=df.to_dict('records')
    )
])


if __name__ == '__main__':
    app.run(debug=True)
