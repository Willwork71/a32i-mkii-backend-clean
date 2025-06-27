from flask import Flask
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Sample data for demonstration
df = pd.DataFrame({
    "country": ["Rwanda", "Mauritius", "Malta", "Ghana", "Saint Kitts"],
    "Carbon Emissions": [100, 150, 130, 180, 120],
    "Renewable Energy %": [60, 75, 70, 50, 65]
})

# Flask server
server = Flask(__name__)

# Dash app
app = Dash(__name__, server=server, url_base_pathname='/')

app.layout = html.Div([
    html.H2("A32i MKII – Country Sustainability Dashboard"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': c, 'value': c} for c in df['country']],
        placeholder="Select a country"
    ),
    dcc.Graph(id='country-graph')
])

@app.callback(
    Output('country-graph', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    if not selected_country:
        return px.line(title="Select a country to view data.")

    country_data = df[df['country'] == selected_country]
    chart_df = country_data.melt(id_vars=["country"], 
                                 value_vars=["Carbon Emissions", "Renewable Energy %"],
                                 var_name="variable", value_name="value")
    
    fig = px.bar(chart_df, x="variable", y="value", color="variable",
                 title=f"Sustainability Indicators for {selected_country}")
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == "__main__":
    app.run(debug=True)
