import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


#import our custom functions
from functions.single_column_value_counts import barplot_single_column_with_filter


app = dash.Dash()


df = pd.read_csv('data/discord_extract.csv')

fig = barplot_single_column_with_filter(df, 'authors', '(Total > 500)')

app.layout = html.Div(children=[
    html.H1(children='Discord Analysis'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    dcc.Graph(figure=fig)
])


if __name__ == '__main__':
    app.run_server(debug=True)

