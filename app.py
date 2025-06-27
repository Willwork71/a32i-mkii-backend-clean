from flask import Flask, request, jsonify
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Sample placeholder data structure for demonstration
def generate_country_data(country):
    # Replace this with real logic or database/API lookup
    carbon = hash(country) % 100 + 100
    renewable = 100 - (hash(country[::-1]) % 60)
    return pd.DataFrame({
        "Metric": ["Carbon Emissions", "Renewable Energy"],
        "Value": [carbon, renewable]
    })

server = Flask(__name__)
app = Dash(__name__, server=server, url_base_pathname='/')

app.layout = html.Div([
    html.H2("A32i MKII – Country Sustainability Dashboard"),
    dcc.Input(id='country-input', type='text', placeholder='Enter a country'),
    dcc.Graph(id='country-graph')
])

@app.callback(
    Output('country-graph', 'figure'),
    Input('country-input', 'value')
)
def update_graph(country):
    if not country:
        return px.line(title="Enter a country name to view data.")
    df = generate_country_data(country)
    return px.bar(df, x='Metric', y='Value', title=f"Sustainability Snapshot: {country}")

if __name__ == '__main__':
    app.run(debug=True)
