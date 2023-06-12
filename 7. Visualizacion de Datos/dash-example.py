# https://plotly.com/examples/


import dash
from dash import dash_table, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import seaborn as sns

app = dash.Dash()
df = sns.load_dataset("titanic")
fig_fare_vs_age = px.scatter(
    df,
    x="fare",
    y="age",
    size="pclass",
    color="alive",
    hover_name="embark_town",
    log_x=True,
    size_max=60,
)
app.layout = html.Div(
    children=[
        html.H1(children="Titanic Dashboard"),
        dash_table.DataTable(
            data=df.to_dict("records"), page_size=9, style_table={"overflowX": "auto"}
        ),
        dcc.Graph(id="fare_vs_age", figure=fig_fare_vs_age),
        # Add interactive callback here
        html.H4("Change the value in the text box to see callbacks in action"),
        html.Div(
            ["Input: ", dcc.Input(id="my-input", value="initial value", type="text")]
        ),
        html.Br(),
        html.Div(id="my-output"),
    ]
)


@app.callback(
    Output(component_id="my-output", component_property="children"),
    Input(component_id="my-input", component_property="value"),
)
def update_output_div(input_value):
    return f"Output: {input_value}"


if __name__ == "__main__":
    app.run_server(debug=True)
