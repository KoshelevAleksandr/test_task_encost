import pandas as pd
import plotly.express as px
from plotly.express.colors import hex_to_rgb
from sqlite3 import connect

pd.set_option('display.max_rows', None)
conn = connect('testDB.db')
df = pd.read_sql("SELECT * from sources", conn)


color_dict = df[['reason', 'color']].set_index('reason').to_dict()['color']
# color_list_hex = [i for i in color_dict.values()]
# for key, value in color_dict.items():
#     color_dict[key] = hex_to_rgb(value)
# color_list = [i for i in color_dict.values()]
print(color_dict)

data_pie = df[['reason', 'duration_hour', 'color']]
df_pie = px.pie(
    data_frame=data_pie,
    values='duration_hour',
    names='reason',
    # color=color_dict,
    # color_discrete_sequence = color_list_hex,
    color_discrete_map=color_dict
)
df_pie.show()