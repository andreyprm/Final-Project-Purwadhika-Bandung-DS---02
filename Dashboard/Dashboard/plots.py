import plotly
import plotly.express as px
import json
import pandas as pd

# convert plotly to JSON
df = pd.read_csv('cleaned_data.csv')

def scatter():
    df = pd.read_csv('cleaned_data.csv')
    # fig = go.Scatter(x = df['MonthlyIncome'],
    # y = df['YearsAtCompany'],
    # text=df['Attrition'],
    # mode='markers')
    fig = px.scatter(df, x="MonthlyIncome", y="YearsAtCompany", color="Attrition")
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def hist():
    df = pd.read_csv('cleaned_data.csv')
    # fig =  dict(
    #         data=[
    #             dict(
    #                 x=df["Gender"],
    #                 y=df["YearsAtCompany"],
    #                 type='bar'
    #             ),
    #         ],
    #         layout=dict(
    #             title='sbsbsbs'
    #         ))
    fig = px.bar(df, x="Gender", y="YearsAtCompany", color="Attrition", barmode="group", facet_col="Department")
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json