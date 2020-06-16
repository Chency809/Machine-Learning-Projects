#!/usr/bin/env python3
# @Time    : 6/3/2020 2:59 PM
# @Author  : Chency Liu
# @School  : Cornell College
# @FileName: test_code_template.py
# @Software: PyCharm
# @Github  : https://github.com/Chency809?tab=repositories



import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import datetime as dt
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(children=[
    html.H1(children='你好，Dash'),

    html.Div(children='''
        Dash: Python网络应用框架'''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': '北京'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': '天津'},
            ],
            'layout': {
                'title': 'Dash数据可视化'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)