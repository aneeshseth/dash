from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px
app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
fig = px.bar(df, x="Amount", y="Fruit")
app.layout = html.Div(children=[
 html.H1(children="hello world!", style={
     "color": colors["text"]
 }),
 dcc.Graph(figure=fig)
])


if __name__ == '__main__':
    app.run(debug=True)