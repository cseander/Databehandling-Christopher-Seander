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