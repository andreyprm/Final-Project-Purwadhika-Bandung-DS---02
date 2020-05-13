import plotly
# import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import json
import pandas as pd

# convert plotly to JSON
def scatter():
    df = pd.read_csv('cleaned_data.csv')
    fig = go.Scatter(x = df['MonthlyIncome'],
    y = df['YearsAtCompany'],
    text=df['Attrition'],
    mode='markers')
    # fig = px.scatter(df, x="MonthlyIncome", y="YearsAtCompany", color="Attrition")
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

# def horsepower():
#     df = pd.read_csv('clean.csv')
#     fig = px.histogram(df, x="horsepower", marginal="rug", hover_data=df.columns)
#     fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#     return fig_json