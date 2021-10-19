import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_columns_missing_data(df):
    missing_values = df[df.columns[df.isnull().any()]]
    ax = sns.barplot(x=missing_values.columns, y=missing_values.isnull().sum())
    ax.set_title("Missing Values")
