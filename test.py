import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
from sqlite3 import connect

conn = connect('testDB.db')
df = pd.read_sql("SELECT * from sources", conn)

df_date = df[['state_begin', 'state_end']].set_index('state_begin')
date_tuples = list(df_date.to_records())

fig = px.timeline(
    data_frame=df,
    x_start='state_begin',
    x_end='state_end',
    color='color',
    hover_name='reason',
    hover_data=['duration_hour']
)
fig.update_xaxes(type='date')
fig.update_layout(barmode="overlay", title_text='Строка состояния')
fig.show()

