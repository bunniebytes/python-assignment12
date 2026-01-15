import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

df = pldata.gapminder(return_type='pandas', datetimes=True)
countries = pd.Series([country for country in df["country"]]).drop_duplicates()

# Initialize Dash app
app = Dash(__name__)
server = app.server

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in countries],
        value="Canada"
    ),
    dcc.Graph(id="gdp-growth")
])

# Callback for dynamic updates
@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(selected_country):
    filtered_df = df[df["country"] == selected_country]
    fig = px.line(filtered_df, x="year", y="gdpPercap", title=f"{selected_country} GDP Per Capita Growth")
    return fig

# Run the app
if __name__ == "__main__": 
    app.run(debug=True) 