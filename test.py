import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
from sqlite3 import connect
from datetime import datetime


conn = connect('testDB.db')
df = pd.read_sql("SELECT * from sources", conn)
print(df["state_end"].max())
date_object = datetime.strptime(df["state_end"].max(), '%Y-%m-%d %H:%M:%S.%f').strftime('%H:%M:%S (%d.%m)')
# time_str = date_object.strftime('%H:%M:%S (%d.%m)')
print(date_object)


# df_date = df[['state_begin', 'state_end']].set_index('state_begin')
# date_tuples = list(df_date.to_records())
# color_list_hex = df['color'].unique()
# print(color_dict)
# color_list_hex = [i for i in color_dict.values()]

# fig_timline = px.timeline(
#     data_frame=df,
#     x_start='state_begin',
#     x_end='state_end',
#     y='endpoint_name',
#     title='График состояния',
#     color='color',
#     color_discrete_sequence=color_list_hex,
#     hover_name='reason',
#     template='plotly_white',
#     custom_data=[
#         'state',
#         'reason',
#         'state_begin',
#         'duration_min',
#         'shift_day',
#         'period_name',
#         'operator',
#     ]
#
# )
# fig_timline.update_layout(
#     yaxis_title='',
#     xaxis={'side': 'top',
#            'title': '',
#            'dtick': 3600000,
#            'tickformat': "%H",
#            },
#     showlegend=False,
#     height=300,
#     title={'x': 0.5},
#     hoverlabel_bgcolor='white',
#     clickmode='select',
#     )
# fig_timline.update_traces(
#     hovertemplate="<br>".join([
#         'Состояние - <b>%{customdata[0]}</b>',
#         'Причина - <b>%{customdata[1]}</b>',
#         'Начало - <b>%{customdata[2]|%H:%M:%S (%d-%m)}</b>',
#         'Длительность - <b>%{customdata[3]:,.2f}</b>',
#         '',
#         'Сменный день - <b>%{customdata[4]|%d-%m-%Y}</b>',
#         'Смена - <b>%{customdata[5]}</b>',
#         'Оператор - <b>%{customdata[6]}</b>'
#     ]),
# )
# fig_timline.show()

