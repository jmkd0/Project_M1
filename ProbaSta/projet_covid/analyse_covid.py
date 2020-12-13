import pandas as pd
import json 
import numpy as np
import matplotlib.pyplot as plt # pip install matplotlib
import plotly.express as px # pip install plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# https://www.data.gouv.fr/en/datasets/donnees-hospitalieres-relatives-a-lepidemie-de-covid-19/#_
hospital_covid = pd.read_csv('https://www.data.gouv.fr/en/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7', sep=';')

hospital_covid = hospital_covid[hospital_covid.columns[1:]]
hospital_covid.columns = ['sexe', 'date', 'hospitalized', 'intensive_case', 'healed_cum','dead_cum']
#Both sex
hospital_covid_both_sex = hospital_covid[hospital_covid['sexe']==0]
hospital_covid_both_sex = hospital_covid_both_sex.groupby('date').sum()
hospital_covid_both_sex = hospital_covid_both_sex.reset_index()

#Male
hospital_covid_male = hospital_covid[hospital_covid['sexe']==1]
hospital_covid_male = hospital_covid_male.drop(columns=["sexe", "date"])
hospital_covid_male = hospital_covid_male.sum()


#Female
hospital_covid_female = hospital_covid[hospital_covid['sexe']==2]
hospital_covid_female = hospital_covid_female.drop(columns=["sexe", "date"])
hospital_covid_female = hospital_covid_female.sum()
print(hospital_covid_female)

#diplay Hospital covid evolution
"""fig = go.Figure()
fig.add_trace(go.Scatter(x=hospital_covid['date'].values, y=hospital_covid['hospitalized'].values, mode='lines+markers', name='Hospitalized cases', marker_color='gold'))
fig.add_trace(go.Scatter(x=hospital_covid['date'].values, y=hospital_covid['intensive_case'].values, mode='lines+markers', name='Intensive cases', marker_color='olive'))
fig.add_trace(go.Scatter(x=hospital_covid['date'].values, y=hospital_covid['healed_cum'].values, mode='lines+markers', name='Cumulative Healed', marker_color='green'))
fig.add_trace(go.Scatter(x=hospital_covid['date'].values, y=hospital_covid['dead_cum'].values, mode='lines+markers', name='Cumulative death', marker_color='red'))
fig.update_layout(title='COVID 19 Hospital information in France', yaxis_zeroline=False, xaxis_zeroline=False)
fig.show()"""


labels = ["Male", "Female"]

night_colors = ['rgb(56, 75, 126)', 'rgb(18, 36, 37)']
sunflowers_colors = ['rgb(177, 127, 38)', 'rgb(205, 152, 36)']
irises_colors = ['rgb(33, 75, 99)', 'rgb(79, 129, 102)']
cafe_colors =  ['rgb(146, 123, 21)', 'rgb(177, 180, 34)']

# Create subplots, using 'domain' type for pie charts
specs = [[{'type':'domain'}, {'type':'domain'}], [{'type':'domain'}, {'type':'domain'}]]
fig = make_subplots(rows=2, cols=2, specs=specs)
fig.add_trace(go.Pie(labels=labels, values=[38, 27], name='Starry Night', marker_colors=night_colors), 1, 1)
fig.add_trace(go.Pie(labels=labels, values=[28, 26], name='Sunflowers', marker_colors=sunflowers_colors), 1, 2)
fig.add_trace(go.Pie(labels=labels, values=[38, 19], name='Irises', marker_colors=irises_colors), 2, 1)
fig.add_trace(go.Pie(labels=labels, values=[31, 24], name='The Night Café', marker_colors=cafe_colors), 2, 2)
fig.update_traces(hoverinfo='label+percent+name', textinfo='label+percent')
fig.update_layout(
    title_text="Global Emissions 1990-2011",
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='GHG',  font_size=20, showarrow=False, yanchor='bottom'),
                 dict(text='CO2',  font_size=20, showarrow=False)])

fig = go.Figure(fig)
fig.show()