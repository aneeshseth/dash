from dash import Dash, dcc, html


app = Dash(__name__)

app.layout = html.Div(children=[
     dcc.Dropdown(['Delhi', 'Karnataka', 'Punjab'], 'Punjab', id='demo-dropdown'),
     dcc.Dropdown(
        ['New York City', 'Montreal', 'San Francisco'],
        ['Montreal', 'San Francisco'],
        multi=True
    ),
    dcc.RadioItems(['New York City', 'Montreal', 'SF'], 'New York City'),
    dcc.Input(placeholder="type here!", type="text"),
    dcc.Checklist(
        ['New York City', 'Montréal', 'San Francisco'],
        ['New York City', 'Montréal']
    ),
   dcc.Slider(
    min=0, max=100, value=30,
    marks={'25': 'mark', '50': '50'}
    )
])


if __name__ == '__main__':
    app.run(debug=True)