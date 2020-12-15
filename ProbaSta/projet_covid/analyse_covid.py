import pandas as pd
import json 
import numpy as np
import matplotlib.pyplot as plt # pip install matplotlib
import plotly.express as px # pip install plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def tests_depistage_covid_datas_france():
    positive_covid = pd.read_csv('https://www.data.gouv.fr/en/datasets/r/dd0de5d9-b5a5-4503-930a-7b08dc0adc7c', sep=';')
    positive_covid_age = positive_covid[['cl_age90', 'P_f', 'P_h', 'P']]
    positive_covid_age = positive_covid_age.groupby('cl_age90').sum()
    positive_covid_age = positive_covid_age.iloc[1:,:]
    positive_covid_age = positive_covid_age.reset_index()
    positive_covid_total = positive_covid_age[['P_h', 'P_f']].sum()
    # Hospital evolution according to ages
    ages = positive_covid_age["cl_age90"].values.tolist()
    specs = [[{'type':'pie'}, {'type':'bar'}], [{'type':'bar'}, {'type':'bar'}]]
    fig_class_age = make_subplots(rows=2, cols=2, specs=specs, subplot_titles=("Plot 1", "Plot 2", "Plot 3", "Plot 4"))
    fig_class_age.add_trace(go.Pie(labels=["Male", "Female"], values=positive_covid_total.values.tolist(), name='Repartition on sex', marker_colors=["#36A2EB", "#BF0060"], hoverinfo='label+percent+name', textinfo='label+percent'), 1, 1)
    fig_class_age.add_trace(go.Bar(x=ages, y=positive_covid_age["P_f"].values.tolist(), name='Females',marker_color='#BF0060'), 1, 2)
    fig_class_age.add_trace(go.Bar(x=ages, y=positive_covid_age["P_h"].values.tolist(), name='Males',marker_color='#36A2EB'), 2, 1)
    fig_class_age.add_trace(go.Bar(x=ages, y=positive_covid_age["P"].values.tolist(), name='Both Sex',marker_color='#7B7B7B'), 2, 2)
    fig_class_age.update_layout(
        title_text="Cas positives en fonction de l'age",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='Repartition based on sex',  font_size=20, showarrow=False),
                     dict(text='Females',  font_size=20, showarrow=False),
                     dict(text='Males',  font_size=20, showarrow=False),
                     dict(text='Both Sex',  font_size=20, showarrow=False)])
    fig_class_age = go.Figure(fig_class_age)
    fig_class_age.show()


    positive_covid_both_sex = positive_covid[['jour', 'P_f', 'P_h', 'P']]
    positive_covid_both_sex = positive_covid_both_sex.groupby('jour').sum()
    positive_covid_both_sex = positive_covid_both_sex.reset_index()
    #diplay Hospital covid evolution
    fig_positive = go.Figure()
    fig_positive.add_trace(go.Scatter(x=positive_covid_both_sex['jour'].values, y=positive_covid_both_sex['P_f'].values, mode='lines', name='Female evolution', marker_color='#BF0060'))
    fig_positive.add_trace(go.Scatter(x=positive_covid_both_sex['jour'].values, y=positive_covid_both_sex['P_h'].values, mode='lines', name='Male evolution', marker_color='#005AB5'))
    fig_positive.add_trace(go.Scatter(x=positive_covid_both_sex['jour'].values, y=positive_covid_both_sex['P'].values, mode='lines', name='All sex evolution', marker_color='#006000'))
    fig_positive.update_layout(title='COVID 19 Positive cases in France', yaxis_zeroline=False, xaxis_zeroline=False)
    fig_positive.show()


def hospitalize_covid_datas_france():
    # https://www.data.gouv.fr/en/datasets/donnees-hospitalieres-relatives-a-lepidemie-de-covid-19/#_
    #### AGE
    hospital_covid_age = pd.read_csv('https://www.data.gouv.fr/en/datasets/r/08c18e08-6780-452d-9b8c-ae244ad529b3', sep=';')
    hospital_covid_age = hospital_covid_age.drop(columns=["reg", "jour"])
    hospital_covid_age = hospital_covid_age.groupby('cl_age90').sum()
    hospital_covid_age = hospital_covid_age.reset_index()
    hospital_covid_age = hospital_covid_age.iloc[1:,:]
    hospital_covid_age.columns = ['class', 'hospitalized', 'intensive', 'healed','dead']

    #### SEX 
    hospital_covid = pd.read_csv('https://www.data.gouv.fr/en/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7', sep=';')
    hospital_covid = hospital_covid[hospital_covid.columns[1:]]
    hospital_covid.columns = ['sexe', 'date', 'hospitalized', 'intensive_case', 'healed_cum','dead_cum']
    #Both sex
    hospital_covid_both_sex = hospital_covid[hospital_covid['sexe']==0]
    hospital_covid_both_sex = hospital_covid_both_sex.groupby('date').sum()
    hospital_covid_both_sex = hospital_covid_both_sex.reset_index()

    ##### SEX
    #Male
    hospital_covid_male = hospital_covid[hospital_covid['sexe']==1]
    hospital_covid_male = hospital_covid_male.drop(columns=["sexe", "date"])
    hospital_covid_male = hospital_covid_male.sum()


    #Female
    hospital_covid_female = hospital_covid[hospital_covid['sexe']==2]
    hospital_covid_female = hospital_covid_female.drop(columns=["sexe", "date"])
    hospital_covid_female = hospital_covid_female.sum()


    hospitalized = [hospital_covid_male["hospitalized"], hospital_covid_female["hospitalized"]]
    intensive = [hospital_covid_male["intensive_case"], hospital_covid_female["intensive_case"]]
    healed = [hospital_covid_male["healed_cum"], hospital_covid_female["healed_cum"]]
    dead = [hospital_covid_male["dead_cum"], hospital_covid_female["dead_cum"]]




    #diplay Hospital covid evolution
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hospital_covid_both_sex['date'].values, y=hospital_covid_both_sex['hospitalized'].values, mode='lines+markers', name='Hospitalized cases', marker_color='gold'))
    fig.add_trace(go.Scatter(x=hospital_covid_both_sex['date'].values, y=hospital_covid_both_sex['intensive_case'].values, mode='lines+markers', name='Intensive cases', marker_color='olive'))
    fig.add_trace(go.Scatter(x=hospital_covid_both_sex['date'].values, y=hospital_covid_both_sex['healed_cum'].values, mode='lines+markers', name='Cumulative Healed', marker_color='green'))
    fig.add_trace(go.Scatter(x=hospital_covid_both_sex['date'].values, y=hospital_covid_both_sex['dead_cum'].values, mode='lines+markers', name='Cumulative death', marker_color='red'))
    fig.update_layout(title='COVID 19 Hospital information in France', yaxis_zeroline=False, xaxis_zeroline=False)
    fig.show()


    # Hospital evolution according to sexs
    specs = [[{'type':'domain'}, {'type':'domain'}], [{'type':'domain'}, {'type':'domain'}]]
    fig_sexe_covid = make_subplots(rows=2, cols=2, specs=specs, subplot_titles=("Plot 1", "Plot 2", "Plot 3", "Plot 4"))
    fig_sexe_covid.add_trace(go.Pie(labels=["Male", "Female"], values=hospitalized, name='Hospitalisation', marker_colors=["#005AB5", "#36A2EB"]), 1, 1)
    fig_sexe_covid.add_trace(go.Pie(labels=["Male", "Female"], values=intensive, name='Réanimation', marker_colors=["#272727", "#7B7B7B"]), 1, 2)
    fig_sexe_covid.add_trace(go.Pie(labels=["Male", "Female"], values=healed, name='Guerison', marker_colors=["#007500", "#02C874"]), 2, 1)
    fig_sexe_covid.add_trace(go.Pie(labels=["Male", "Female"], values=dead, name='Mortalité', marker_colors=["#BF0060", "#FF6384"]), 2, 2)
    fig_sexe_covid.update_traces(hoverinfo='label+percent+name', textinfo='label+percent')
    fig_sexe_covid.update_layout(
        title_text="Prsonnes hospitalisées en fonction du sexe",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='Hospitalisation',  font_size=20, showarrow=False),
                     dict(text='Réanimation',  font_size=20, showarrow=False),
                     dict(text='Guerison',  font_size=20, showarrow=False),
                     dict(text='Mortalité',  font_size=20, showarrow=False)])
    fig_sexe_covid = go.Figure(fig_sexe_covid)
    fig_sexe_covid.show()


    # Hospital evolution according to ages
    ages = hospital_covid_age["class"].values.tolist()
    fig_class_age = make_subplots(rows=2, cols=2, shared_xaxes=True, subplot_titles=("Plot 1", "Plot 2", "Plot 3", "Plot 4"))
    fig_class_age.append_trace(go.Bar(x=ages, y=hospital_covid_age["hospitalized"].values.tolist(), name='Hospitalied',marker_color='#36A2EB'), 1, 1)
    fig_class_age.append_trace(go.Bar(x=ages, y=hospital_covid_age["intensive"].values.tolist(), name='Under intensive  care',marker_color='#7B7B7B'), 1, 2)
    fig_class_age.append_trace(go.Bar(x=ages, y=hospital_covid_age["healed"].values.tolist(), name='Recovered',marker_color='#02C874'), 2, 1)
    fig_class_age.append_trace(go.Bar(x=ages, y=hospital_covid_age["dead"].values.tolist(), name='Dead',marker_color='#BF0060'), 2, 2)
    fig_class_age.update_layout(
        title_text="Personnes hospitalisées en fonction de la tranche d'age",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='Hospitalisation',  font_size=20, showarrow=False),
                     dict(text='Réanimation',  font_size=20, showarrow=False),
                     dict(text='Guerison',  font_size=20, showarrow=False),
                     dict(text='Mortalité',  font_size=20, showarrow=False)])
    fig_class_age = go.Figure(fig_class_age)
    fig_class_age.show()



hospitalize_covid_datas_france()

tests_depistage_covid_datas_france()
