import pandas as pd     
import plotly           
import plotly.express as px
import dash             
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import os


os.chdir("C:\Users\dsikk\VSCode\DAD\clusters\maps\dash_gh")
FILE = "clusters_labeled.csv"
df = pd.read_csv(FILE, dtype={"fips":str}).drop(columns=['Unnamed: 0'])

clusters = ['4_clusters', '5_clusters', '6_clusters',
     '7_clusters', '8_clusters']

dropdown_options = [
    {'label': '4 Clusters', 'value': '4_clusters'},
    {'label': '5 Clusters', 'value': '5_clusters'},
    {'label': '6 Clusters', 'value': '6_clusters'},
    {'label': '7 Clusters', 'value': '7_clusters'},
    {'label': '8 Clusters', 'value': '8_clusters'}]

clusters_8_dict = {1:"EP-Least", 2:"Cath-Less", 3:"EP-Less", 4:"Other-LDS", 
                  5: "Cath-High", 6:"MP, Cath", 7:"Pluralistic", 8:"EP-High"}
color_map = {"Catholic":"red", "Cath":"red","Cath-High":"red", "Cath-Less":"orange",
             "EP":"black","EP-High":"black", "EP-Less":"blue", "EP-Least":"lightblue",
             "Other-LDS": "green",
             "Pluralistic": "grey",
             "MP, Cath": "purple", "MP,Cath":"purple"
             }
# Create the Dash app
app = dash.Dash(__name__)

#drop down menu
app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options = dropdown_options,
        value = "4_clusters"
    ),
    html.Hr(),
    dcc.Graph(id='display-selected-values'),
])

@app.callback(
    dash.dependencies.Output('display-selected-values', 'figure'),
    [dash.dependencies.Input('dropdown', 'value')])

def update_output(value):
    fig = px.choropleth(df, geojson='https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json', 
        locations='fips', 
        hover_name="fips",
        color=value,
        #color_discrete_sequence=px.colors.qualitative.G10,
        color_discrete_map=color_map,
        scope="usa",
        title = "Religious Clusters in the United States",
        width = 1000,
        height = 600)
    return fig 

if __name__ == '__main__':
    app.run_server()