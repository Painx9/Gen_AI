import dash
from dash import dcc, html, Input, Output
import pandas as pd
import numpy as np
import joblib

# Load the saved model and dataset
model = joblib.load('model.pkl')
sonar_data = pd.read_csv('sonar data.csv', header=None)

# Initialize the Dash application
app = dash.Dash(__name__)
server = app.server

# Define the user interface layout
app.layout = html.Div(style={
    'fontFamily': 'Arial, sans-serif', 
    'padding': '30px', 
    'maxWidth': '900px', 
    'margin': '0 auto', 
    'backgroundColor': '#f9f9f9'
}, children=[
    
    html.H1("Sonar Navigation: Rock vs. Mine Dashboard", style={'textAlign': 'center', 'color': '#2C3E50'}),
    html.P("An interactive web app built with Dash to analyze sonar return frequencies and evaluate machine learning predictions.", style={'textAlign': 'center', 'color': '#555'}),
    
    html.Hr(),
    
    # Tabs to organize content
    dcc.Tabs(id="dashboard-tabs", value='tab-overview', children=[
        
        # Tab 1: Dataset Overview & Visualizations
        dcc.Tab(label='Dataset Overview', children=[
            html.Div(style={'padding': '20px', 'backgroundColor': 'white', 'marginTop': '10px', 'borderRadius': '5px'}, children=[
                html.H3("Dataset Summary"),
                html.P(f"Total Rows (Samples): {sonar_data.shape[0]}"),
                html.P(f"Total Columns (Sonar Frequencies + Label): {sonar_data.shape[1]}"),
                
                # Class Distribution Bar Chart
                dcc.Graph(
                    id='class-distribution',
                    figure={
                        'data': [{
                            'x': ['Mine (M)', 'Rock (R)'], 
                            'y': sonar_data[60].value_counts().reindex(['M', 'R']), 
                            'type': 'bar', 
                            'marker': {'color': ['#E74C3C', '#3498DB']}
                        }],
                        'layout': {
                            'title': 'Distribution of Rocks vs. Mines in Dataset',
                            'xaxis': {'title': 'Object Class'},
                            'yaxis': {'title': 'Count'}
                        }
                    }
                )
            ])
        ]),
        
        # Tab 2: Make Predictions
        dcc.Tab(label='Make a Prediction', children=[
            html.Div(style={'padding': '20px', 'backgroundColor': 'white', 'marginTop': '10px', 'borderRadius': '5px'}, children=[
                html.H3("Test Sonar Instance Prediction"),
                html.P("Click the button below to test a sample instance from the dataset through your Logistic Regression model."),
                
                html.Button('Run Prediction on Sample', id='predict-btn', n_clicks=0, style={
                    'padding': '10px 20px', 
                    'backgroundColor': '#2ECC71', 
                    'color': 'white', 
                    'border': 'none', 
                    'borderRadius': '4px',
                    'cursor': 'pointer',
                    'fontSize': '16px'
                }),
                
                html.Div(id='prediction-output', style={'marginTop': '25px', 'fontSize': '20px', 'fontWeight': 'bold'})
            ])
        ])
    ])
])

# Callback to handle predictions dynamically when button is clicked
@app.callback(
    Output('prediction-output', 'children'),
    Input('predict-btn', 'n_clicks')
)
def update_prediction(n_clicks):
    if n_clicks > 0:
        # Grab a sample row from dataset features (Row 0)
        sample_input = sonar_data.drop(columns=60).iloc[0].values.reshape(1, -1)
        pred = model.predict(sample_input)[0]
        
        result_text = "Mine (M)" if pred == 'M' else "Rock (R)"
        color = '#E74C3C' if pred == 'M' else '#3498DB'
        
        return html.Div([
            html.Span("Prediction Result: "),
            html.Span(f"{result_text}", style={'color': color})
        ])
    return "Click the button above to run a prediction."

if __name__ == '__main__':
    app.run(debug=True)
