from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.P(children="hello world")
])

if __name__ == '__main__':
    app.run(debug=True)
