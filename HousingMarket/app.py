import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table as dt
from dash.dependencies import Input, Output
import pandas as pd
from dash.dependencies import Input
from dash.dependencies import Output


df = pd.read_csv('df')

app = dash.Dash(__name__)

states = df.state_name.unique().tolist()

app.layout = html.Div([
    html.Div(
           className="media-body text-center",
           children=[
           html.H1('The Next Big City')], style={'textAlign': 'center'}
        
    ),
    html.Div(
           className = "container",
           children=[
           html.Img(src='static/images/NBC_3.jpg',
                    style={
                        'height': '20%',
                        'width': '70%'
                    })
           
         ], style={'textAlign': 'center'}
        
    ),
    html.Div(
    children=[
        dcc.Dropdown(
            id="filter_dropdown",
            options=[{"label": st, "value": st} for st in states],
            placeholder="-Select a State-",
            multi=True,
            value=df.state_name.values,
        ),
        dt.DataTable(
            id="table-container",
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("records")
        )
    ])
])


@app.callback(
    Output("table-container", "data"),
    Input("filter_dropdown", "value") 
)
def display_table(state):
    dff = df[df.state_name.isin(state)]
    return dff.to_dict("records")

if __name__ == '__main__':
    app.run_server(debug=True)