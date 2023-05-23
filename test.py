import plotly.express as px
from sqlite3 import connect
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots

search = ['Наладка', 'Короткая остановка']
conn = connect('./testDB.db')
df = pd.read_sql(f"SELECT * from sources ", conn)
df.insert(1, 'visibility', 1)
for i in search:
    df.loc[df['reason'] == i, 'visibility'] = 0.5
df1 = df.loc[df['visibility'] == 0.5]
df2 = df.loc[df['visibility'] == 1]
print(df1)


color_list_hex = df['color'].unique()

fig1 = px.timeline(
    data_frame=df1,
    x_start='state_begin',
    x_end='state_end',
    y='endpoint_name',
    title='График состояния',
    color='color',
    color_discrete_sequence=color_list_hex,
    hover_name='reason',
    opacity = 0.5,
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
fig1.update_layout(
    yaxis_title='',
    xaxis={'side': 'top',
           'title': '',
           'dtick': 3600000,
           'tickformat': "%H",
           },
    showlegend=False,
    # legend_itemclick='toggleothers',
    height=300,
    title={'x': 0.5},
    hoverlabel_bgcolor='white',
    clickmode='select',
    )
template_timeline = '<br>'.join([
        'Состояние - <b>%{customdata[0]}</b>',
        'Причина - <b>%{customdata[1]}</b>',
        'Начало - <b>%{customdata[2]|%H:%M:%S (%d-%m)}</b>',
        'Длительность - <b>%{customdata[3]:,.2f}</b> мин.',
        '',
        'Сменный день - <b>%{customdata[4]|%d-%m-%Y}</b>',
        'Смена - <b>%{customdata[5]}</b>',
        'Оператор - <b>%{customdata[6]}</b><extra></extra>'
    ])
for c in df.columns:
    fig1 = fig1.add_trace(
        go.Trace(
            data_frame=df2,
            x_start='state_begin',
            x_end='state_end',
            color='color',
            color_discrete_sequence=color_list_hex,
            hover_name='reason',
            opacity=1,
            template='plotly_white',
        ))
fig1.update_traces(
        hovertemplate=template_timeline,
    )
# fig1.show()