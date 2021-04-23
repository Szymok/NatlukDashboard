import pandas as pd
import plotly.express as px


def barplot_single_column_with_filter(df, column, filter = None):
    authors = df['author'].value_counts().reset_index()
    authors.columns = [column.capitalize(), 'Total']
    if filter:
        authors = authors.query(filter)
    fig_bar = px.bar(data_frame=authors, x=column.capitalize(), y='Total', log_y=True)

    return fig_bar