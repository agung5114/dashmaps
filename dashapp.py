import dash
import dash_html_components as html
import json
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import geopandas as gpd
from geojson_rewind import rewind

f = gpd.read_file('maps.json',)
geo_ur = json.loads(f.to_json())
geo = rewind(geo_ur,rfc7946=False)

df = pd.read_csv('maps.csv', sep=';')
df['CC_1'] = df['CC_1'].astype(int)
df['VARNAME_1'] = df['VARNAME_1'].astype(int)

fig = px.choropleth(df, geojson=geo,locations="GID_1", color="VARNAME_1",hover_name = "NAME_1",featureidkey="properties.GID_1",
color_discrete_sequence=None, color_discrete_map={},range_color=[1,100],color_continuous_scale='Rainbow')

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="choropleth", figure=fig),
])

if __name__ == "__main__":
    app.run_server(debug=False, port=8002)