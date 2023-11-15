from dash import Dash, dcc, html, Input, Output, State, callback



app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='Montréal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])


@callback(Output('output-state', 'children'),
              Input('submit-button-state', 'n_clicks'),
              State('input-1-state', 'value'),
              State('input-2-state', 'value'))
def update_output(n_clicks, input1, input2):
    return f'''
        Input 1 is "{input1}",
        and Input 2 is "{input2}"
    '''


if __name__ == '__main__':
    app.run(debug=True)
