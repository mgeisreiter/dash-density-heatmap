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
app.title='earthquakes'

########## Define the figure

quakes = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

import plotly.graph_objects as go
fig = go.Figure(go.Densitymapbox(lat=quakes.Latitude, lon=quakes.Longitude, z=quakes.Magnitude, radius=10))
fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


########### Set up the layout

app.layout = html.Div(children=[
    html.H1('Earthquakes'),
    html.Div([
        dcc.Graph(id='quakes', figure=fig),
        html.A('Code on Github', href='https://github.com/austinlasseter/dash-density-heatmap'),
        html.Br(),
        html.A('Source:', href='https://plot.ly/python/mapbox-density-heatmaps')
    ])
])


############ Execute the app
if __name__ == '__main__':
    app.run_server(debug=True)
