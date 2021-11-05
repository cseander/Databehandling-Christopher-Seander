import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

def px_line(data, x, y, title, labels, save_location) -> None:
    fig = px.line(data, x=x, y=y, title=title, labels=labels)
    fig.write_html(save_location)
    fig.show()

def combine_year_week_numer(df) -> pd.Series:
    return df["år"].astype(str) + "v" + df["veckonummer"].astype(str)

def px_multiple_line(data, plot_title, legend_title, yaxis, xaxis, save_location) -> None:
    fig = px.line(data, title=plot_title)
    fig.update_layout(legend_title=legend_title, yaxis_title=yaxis, xaxis_title=xaxis)
    fig.write_html(save_location)
    fig.show()