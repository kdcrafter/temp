import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from time import sleep

from us_today import us_layout

def test_us001_simple_example(dash_duo):
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    app.layout = us_layout

    dash_duo.start_server(app)
    dash_duo.driver.maximize_window()

    # dash_duo.find_element('#example-graph')
    # dash_duo.wait_for_element('#example-graph')
    # dash_duo.wait_for_element_by_css_selector('#example-graph')
    # dash_duo.wait_for_element_by_id('example-graph')

    # graph = dash_duo.find_element('#example-graph')
    # graph.screenshot('temp.png')

    # dash_duo.percy_snapshot('us001_example', wait_for_callbacks=True)
    sleep(5)
    dash_duo.percy_snapshot('us001_example')
