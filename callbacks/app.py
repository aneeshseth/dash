from dash import Dash, html, dcc, Input, Output, callback
app = Dash(__name__)


app.layout = html.Div(children=[
   dcc.Input(placeholder="type here!", type="text", id="input_val"),
   html.Div(children="", id="output_div")
])

@callback(
    Output('output_div', 'children'),
    Input('input_val', 'value')
)
def updateOutput(output):
    return f'the current string is at {output}'

if __name__ == '__main__':
    app.run(debug=True)
