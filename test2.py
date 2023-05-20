import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
from sqlite3 import connect

conn = connect('testDB.db')
df = pd.read_sql("SELECT * from sources", conn)


df1 = pd.DataFrame([
dict(unit='MVT',Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
dict(unit='MVT',Task="Job B", Start='2009-02-28', Finish='2009-04-15'),
dict(unit='MVT',Task="Job A", Start='2009-04-15', Finish='2009-05-30')
])

df2 = pd.DataFrame([
    dict(unit='MVT',Task="Job A", Start='2009-01-15', Finish='2009-02-15'),
    dict(unit='MVT',Task="Job B", Start='2009-02-15', Finish='2009-04-28'),
    dict(unit='MVT',Task="Job A", Start='2009-04-28', Finish='2009-05-30')
])

fig1 = px.timeline(df1, x_start="Start", x_end="Finish", y="unit",color="Task")
fig2 = px.timeline(df2, x_start="Start", x_end="Finish", y="unit",color="Task")


fig_sub = make_subplots(rows=2,shared_xaxes=True,)
for i in range(0,len(fig1['data'])):
    fig_sub.append_trace(fig1['data'][i], row=1, col=1)


for i in range(0,len(fig2['data'])):
    fig_sub.append_trace(fig2['data'][i], row=2, col=1)

fig_sub.update_xaxes(type='date')
fig_sub.update_layout(barmode="overlay", title_text='Строка состояния')
fig_sub.show()