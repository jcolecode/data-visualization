import dash
import json
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
from urllib.request import urlopen
from dash.dependencies import Input, Output, State

app = dash.Dash(
    __name__,
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1.0"
        }
    ],

    # Include custom stylesheets here
    external_stylesheets=[
        'https://codepen.io/chriddyp/pen/bWLwgP.css'
    ],

    # Include custom js here
    external_scripts=[],
    suppress_callback_exceptions=True
)

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# Search through dataset
df = pd.read_csv("illinoisData.csv", dtype={"fips": str})

### Build a figure for dataset
fig = px.choropleth(df, geojson=counties, locations='fips', color='total_cases',
                           color_continuous_scale="ylorrd",
                           range_color=(0, 710000),
                           scope="usa",
                           hover_name='county',
                           labels={'total_cases':'Total Covid Cases'}
                          )
fig.update_geos(fitbounds='locations', visible=False)
fig.show()

app.layout = html.Div(
    [
        html.H1("Yo"),

        html.Div("Dash: A web application framework for python"),

        dcc.Graph(id='graph', figure=fig),
    ] 
)


if __name__ == "__main__":
    app.run_server(host='0.0.0.0')