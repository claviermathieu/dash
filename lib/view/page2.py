import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html



import plotly.express as px
import pandas as pd

def page2():


    page2 = html.Div([
        html.H1("Test"),
        dbc.Row(
            dbc.Col(html.Div("A single, half-width column"), width=6)
            ),
        dbc.Row(
            dbc.Col(html.Div("An automatically sized column"), width="auto")
        ),
        dbc.Row([
            dbc.Col(html.Div("One of three columns"), width=3),
            dbc.Col(html.Div("One of three columns")),
            dbc.Col(html.Div("One of three columns"), width=3),
        ])
    ])

    return(page2)