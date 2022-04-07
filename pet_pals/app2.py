import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table as dt
from dash.dependencies import Input, Output
import pandas as pd
from dash.dependencies import Input
from dash.dependencies import Output


df = pd.read_csv('df')

app = dash.Dash(__name__,  
    assets_external_path='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa',
    )
    
    #'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u',
    #'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp'
                


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
           html.Img(src='../static/images/NBC_3.jpg',
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