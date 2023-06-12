# https://plotly.com/examples/
# https://dash.plotly.com/basic-callbacks
# https://dash-example-index.herokuapp.com

import dash
from dash import dash_table, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import seaborn as sns

app = dash.Dash()
df = sns.load_dataset("titanic")

app.layout = html.Div(
    children=[
        html.H1(
            children="Titanic Dashboard",
            style={"text-align": "center"},
        ),
        html.Div(
            [dcc.Dropdown(df.columns, "fare", id="xaxis-column")],
            style={"width": "48%", "display": "inline-block"},
        ),
        html.Div(
            [dcc.Dropdown(df.columns, "age", id="yaxis-column")],
            style={"width": "48%", "display": "inline-block"},
        ),
        html.Div(
            [dcc.RadioItems(["Pie", "Scatter"], "Pie", id="graph-type")],
            style={"width": "48%", "display": "inline-block"},
        ),
        dcc.Graph(id="scatter"),
        html.Div(
            [dcc.Dropdown(df.columns, "pclass", id="names")],
            style={"width": "48%", "display": "inline-block"},
        ),
        dcc.Graph(id="pie"),
        dash_table.DataTable(
            data=df.to_dict("records"), page_size=9, style_table={"overflowX": "auto"}
        ),
    ]
)


@app.callback(
    Output(component_id="scatter", component_property="figure"),
    Input("xaxis-column", "value"),
    Input("yaxis-column", "value"),
    Input("graph-type", "value"),
)
def update_scatter(xaxis_column_name, yaxis_column_name, graph_type):
    if graph_type == "Scatter":
        return px.scatter(
            df,
            x=xaxis_column_name,
            y=yaxis_column_name,
        )
    elif graph_type == "Pie":
        return px.pie(
            df,
            names=xaxis_column_name,
        )


@app.callback(
    Output(component_id="pie", component_property="figure"),
    Input("names", "value"),
)
def update_pie(
    column_name,
):
    return px.pie(
        df,
        names=column_name,
    )


if __name__ == "__main__":
    app.run_server(debug=True)
