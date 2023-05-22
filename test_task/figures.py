import plotly.express as px


def get_pie(df):
    color_list_hex = df['color'].unique()
    fig_pie = px.pie(
        data_frame=df,
        values='duration_hour',
        names='reason',
        color='color',
        color_discrete_sequence=color_list_hex,
    )
    template_pie = "<br>".join([
            'Состояние - <b>%{label}</b>',
            'Длительность - <b>%{value:,.2f} час.</b>'
        ])
    fig_pie.update_traces(
        hovertemplate=template_pie,
    )
    return fig_pie


def get_timline(df):
    color_list_hex = df['color'].unique()
    fig_timline = px.timeline(
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
    fig_timline.update_layout(
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
            'Оператор - <b>%{customdata[6]}</b>'
        ])
    fig_timline.update_traces(
        hovertemplate=template_timeline,
    )
    return fig_timline