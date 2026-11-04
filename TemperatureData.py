# "Create a dashboard showing temperature data over time. "
# "Include both a line chart and a summary statistics card "
# "showing min, max, and average temperature."

from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

app = Dash(__name__)

data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'Temperature': [22, 25, 23, 27, 24],
    'City': ['Sydney', 'Sydney', 'Sydney', 'Sydney', 'Sydney']
}

df = pd.DataFrame(data)

app.layout = html.Div([
    html.H1("Temperature Data", style={'textAlign': 'center'}),
    dcc.Graph(id='temperature-graph'),
    html.Div(id='summary-stats', style={'textAlign': 'center', 'fontSize': 20})
])

@app.callback(
    [Output('temperature-graph', 'figure'),
     Output('summary-stats', 'children')],
     [Input('temperature-graph', 'id')]
)
def update_dashboard(_):
    fig = px.line(
        df,
        x ='Date',
        y ='Temperature',
        title ='Temperature Data Over Time',
        labels = {'Temperature': 'Temperature (C)', 'Date': 'Date'}
    )

    min_temp = df['Temperature'].min()
    max_temp = df['Temperature'].max()
    avg_temp = df['Temperature'].mean()

    summary = f'Min: {min_temp} C | Max: {max_temp} C | Avg: {avg_temp:.2f} C'

    return fig, summary

if __name__ == '__main__':
    app.run(debug=True)