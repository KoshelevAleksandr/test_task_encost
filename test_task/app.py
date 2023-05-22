from dash import html, Output, Input, State, dcc
from dash_extensions.enrich import (DashProxy,
                                    ServersideOutputTransform,
                                    MultiplexerTransform)
import dash_mantine_components as dmc
from dash.exceptions import PreventUpdate
from sqlite3 import connect
import pandas as pd
from datetime import datetime
import figures


CARD_STYLE = dict(withBorder=True,
                  shadow="sm",
                  radius="md",
                  style={'height': '400px'})


class EncostDash(DashProxy):
    def __init__(self, **kwargs):
        self.app_container = None
        super().__init__(transforms=[ServersideOutputTransform(),
                                     MultiplexerTransform()], **kwargs)


app = EncostDash(name=__name__)

conn = connect('../testDB.db')
df = pd.read_sql("SELECT * from sources", conn)

client_name = df["client_name"][0]
shift_day = df["shift_day"][0]
endpoint_name = df["endpoint_name"][0]
state_begin = datetime.strptime(df["state_begin"].min(), "%Y-%m-%d %H:%M:%S.%f").strftime("%H:%M:%S (%d.%m)")
state_end = datetime.strptime(df["state_end"].max(), "%Y-%m-%d %H:%M:%S.%f").strftime("%H:%M:%S (%d.%m)")


def get_layout():
    return html.Div([
        dmc.Paper([
            dmc.Grid([
                dmc.Col([
                    dmc.Card([
                        html.Div(children=[
                            html.H1(f'Клиент: {client_name}'),
                            html.H4([
                                html.Div(f'Сменный день: {shift_day}'),
                                html.Div(f'Точка учета: {endpoint_name}'),
                                html.Div(f'Начало периода: {state_begin}'),
                                html.Div(f'Конец периода: {state_end}')
                            ]),
                            dcc.Dropdown(
                                df.reason.unique(),
                                id='input',
                                multi=True,
                                placeholder=''),
                        ]),
                        dmc.Button(
                            'Фильтровать',
                            id='button1'),
                        html.Div(
                            id='output')],
                        **CARD_STYLE)
                ], span=6),
                dmc.Col([
                    dmc.Card([
                        html.Div(dcc.Graph(
                            id='fig_pie',
                            figure=figures.get_pie(df)))],
                        **CARD_STYLE
                        )
                ], span=6),
                dmc.Col([
                    dmc.Card([
                        html.Div(dcc.Graph(
                            id='fig_timline',
                            figure=figures.get_timline(df)))],
                        **CARD_STYLE)
                ], span=12),
            ], gutter="xl",)
        ])
    ])


app.layout = get_layout()

# @app.callback(
#     Output(component_id='fig_timline', component_property='figure'),
#     Input(component_id='dropdown-selection', component_property='value')
# )
# def update_graph(col_chosen):
#     pass
#
#     return f'Первая кнопка нажата, данные:'


@app.callback(
    Output('output', 'children'),
    State('input', 'value'),
    Input('button1', 'n_clicks'),
    prevent_initial_call=True,
)
def update_div2(
    value,
    click
):
    if click is None:
        raise PreventUpdate

    return f'Вторая кнопка нажата, данные: {value}'


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
