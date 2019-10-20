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
app.title='dc_houses'

########## Define the data
df = pd.read_csv('resources/DC_Properties.csv', index_col='Unnamed: 0')
df=df[df['PRICE'].between(300000, 500000)] # artificially reduce the number of data points for efficiency

########## Define the figure

fig = go.Figure(go.Densitymapbox(lat=df['LATITUDE'], lon=df['LONGITUDE'], z=df['PRICE'], radius=10))
fig.update_layout(mapbox_style="stamen-terrain",
                  mapbox_center_lon=-77.07,
                  mapbox_center_lat=38.92,
                  mapbox_zoom=11,
                 )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

########### Set up the layout

app.layout = html.Div(children=[
    html.H1('DC Houses'),
    html.Div([
        dcc.Graph(id='figure-1', figure=fig),
        html.A('Code on Github', href='https://github.com/austinlasseter/dash-density-heatmap'),
        html.Br(),
        html.A('Source:', href='https://plot.ly/python/mapbox-density-heatmaps')
    ])
])


############ Execute the app
if __name__ == '__main__':
    app.run_server(debug=True)
