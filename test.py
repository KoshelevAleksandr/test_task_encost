import pandas as pd
import plotly.express as px
from sqlite3 import connect


conn = connect('testDB.db')
df = pd.read_sql("SELECT * from sources", conn)

data_pie = df[['reason', 'duration_hour']]
dic = {key: value for key, value in zip(df['reason'], df['color'])}
print(dic)
# df_pie = px.pie(
#     data_frame=data_pie,
#     values='duration_hour',
#     names='reason',
#     color_discrete_map={key: value for key, value in zip(df['reason'], df['color'])})
# df_pie.show()