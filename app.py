import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pandas as pd
import pickle

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='DC Crime 🚨'

########## Define the data
df = pd.read_csv('resources/crime_incidents_new.csv')

###### Set up variables
list_of_choices=['Homicide', 'Robbery', 'Motor Vehicle Theft', 'Burglary', 'Arson']

########## Define the figure

def generateFigure(offense):
    df_filtered = df[df['OFFENSE'] == offense.upper()]
    fig = go.Figure(go.Densitymapbox(lat=df_filtered['LATITUDE'], lon=df_filtered['LONGITUDE'], z=df_filtered['Count'], radius=10))
    fig.update_layout(mapbox_style="stamen-terrain",
                    mapbox_center_lon=-77.07,
                    mapbox_center_lat=38.92,
                    mapbox_zoom=11,
                    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig


########### Set up the layout

app.layout = html.Div(children=[
    html.H1('Crime in DC'),
    html.H3('Select an Offense'),
    html.Br(),
    dcc.Dropdown(id='your-input-here',
            options=[{'label': i, 'value': i} for i in list_of_choices],
            value='Homicide',
            style={'width': '500px'}),
    html.Br(),
    html.Div([
        dcc.Graph(id='figure-1', figure=generateFigure('OFFENSE')),
        html.A('Code on Github', href='https://github.com/mgeisreiter/dash-density-heatmap'),
        html.Br(),
        html.A('Source:', href='https://plot.ly/python/mapbox-density-heatmaps')
    ])
])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('figure-1', 'figure'),
              [dash.dependencies.Input('your-input-here', 'value')])
def updateFig(whatever_you_chose):
    return generateFigure(whatever_you_chose)



############ Execute the app
if __name__ == '__main__':
    app.run_server(debug=True)
