import pandas as pd
import plotly
import plotly.graph_objs as go
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Load the data from a CSV file
    df = pd.read_csv('startups.csv')

    # Filter for AI startups
    df_ai = df[df['category'] == 'AI']

    # Count the number of AI startups founded each year
    ai_trends = df_ai.groupby('founding_year').size()

    # Create the plotly figure
    fig = go.Figure(data=go.Scatter(x=list(ai_trends.index), y=list(ai_trends.values)))
    
    # Convert the figure to JSON
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    # Render the index.html template and pass in the figure in JSON format
    return render_template('index.html', fig_json=fig_json)

if __name__ == '__main__':
    app.run(debug=True)

