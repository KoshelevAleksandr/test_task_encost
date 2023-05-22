import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
from sqlite3 import connect

conn = connect('testDB.db')
df = pd.read_sql("SELECT * from sources", conn)

df_date = df[['state_begin', 'state_end']].set_index('state_begin')
date_tuples = list(df_date.to_records())
color_dict = df[['reason', 'color']].set_index('reason').to_dict()['color']
color_list_hex = [i for i in color_dict.values()]

fig = px.timeline(
    data_frame=df,
    x_start='state_begin',
    x_end='state_end',
    y='endpoint_name',
    title='График состояния',
    color='color',
    color_discrete_sequence=color_list_hex,
    hover_name='reason',
    template='plotly_white',
    custom_data=[
        'state',
        'reason',
        'state_begin',
        'duration_min',
        'shift_day',
        'period_name',
        'operator',
    ]

)
fig.update_layout(
    yaxis_title='',
    # xaxis_title='',
    xaxis={'side': 'top',
           'title': '',
           },
    showlegend=False,
    height=300,
    title={'x': 0.5},
    hoverlabel_bgcolor='white',
    clickmode='select',
    )
fig.update_traces(
    hovertemplate="<br>".join([
        'Состояние - <b>%{customdata[0]}</b>',
        'Причина - <b>%{customdata[1]}</b>',
        'Начало - <b>%{customdata[2]|%H:%M:%S (%d-%m)}</b>',
        'Длительность - <b>%{customdata[3]:,.2f}</b>',
        '',
        'Сменный день - <b>%{customdata[4]|%d-%m-%Y}</b>',
        'Смена - <b>%{customdata[5]}</b>',
        'Оператор - <b>%{customdata[6]}</b>'
    ]),


)
fig.show()

