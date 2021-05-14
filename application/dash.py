import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
import dash_table
import sidetable as stb
import datetime
from datetime import datetime, timedelta
from datetime import date
import geopandas as gpd
import flask
import os
yesterday = datetime.now() - timedelta(1)
yea = datetime.strftime(yesterday, '%Y%m%d')

today = date.today()
d2 = today.strftime("Fecha de actualización : %d-%m-%Y")







###############################
# DATABASES
############################### Abre archivos

base = pd.read_csv('https://raw.githubusercontent.com/fdealbam/CamaraDiputados/main/application/mun_p1_cvegeo.csv', encoding='latin-1', usecols=['Nom_Ent','nom_mun','cve_ent_mun1','cve_ent_mun2'])
contagios = pd.read_csv("https://datos.covid-19.conacyt.mx/Downloads/Files/Casos_Diarios_Municipio_Confirmados_%s.csv" %(yea))
#decesos= pd.read_csv("https://raw.githubusercontent.com/fdealbam/CamaraDiputados/main/Casos_Diarios_Municipio_Defunciones_20210312.csv")
decesos = pd.read_csv("https://datos.covid-19.conacyt.mx/Downloads/Files/Casos_Diarios_Municipio_Defunciones_%s.csv" %(yea))
SS = ('https://datos.covid-19.conacyt.mx/')
autores = ('https://raw.githubusercontent.com/winik-pg/exercises_pythoncitos/master/Autores.docx')
entidades  =  pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv" )

pasa= pd.read_csv('https://raw.githubusercontent.com/winik-pg/exercises_pythoncitos/master/000_comorbilidades.csv')
titulos=['cve_geo1','cve_ent', 'decesos_60_y_mas']
muertos60_mas = pd.read_csv('https://raw.githubusercontent.com/winik-pg/exercises_pythoncitos/master/muertes_60%2B.csv', names=titulos)

aa = pd.read_csv("https://raw.githubusercontent.com/fdealbam/CamaraDiputados/main/application/Tabla%202.%20Confirmados%20por%20semana.csv")
aa.groupby("Nom_Ent").sum().to_csv("00.csv")
sem_edos= pd.read_csv("00.csv")
sem_edos

ee = pd.read_csv("https://raw.githubusercontent.com/fdealbam/CamaraDiputados/main/application/Tabla%201.%20Confirmados%20mensuales.csv")
ee.groupby("Nom_Ent").sum().to_csv("00.csv")
mes_edos= pd.read_csv("00.csv")




#- FILE JSON ------------------------------------------------------------------------------

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/Aeelen-Miranda/exercises_pythoncitos/master/mexico.json') as response:
    counties = json.load(response)
counties["features"][0]

# Creacion de geodataframe
geo_df = gpd.GeoDataFrame.from_features(counties["features"])

geo_df.replace(['Coahuila',
                'Distrito Federal',
                'Michoacán',
                'Veracruz'],
               #por
                 ['Coahuila de Zaragoza',
                 'Ciudad de México',
                 'Michoacán de Ocampo',
                  'Veracruz de Ignacio de la Llave'],inplace=True)
# Merge 
concat0 = geo_df.merge(mes_edos, left_on= "name", right_on= "Nom_Ent", how= "right")

# Selección de columnas 
concat2 = concat0[
    ['geometry',
    'Nom_Ent',
       'cve_ent', 'poblacion', 'Total', 'febrero20', 'marzo20',
       'abril20', 'mayo20', 'junio20', 'julio20', 'agosto20', 'septiembre20',
       'octubre20', 'noviembre20', 'diciembre20', 'enero21', 'febrero21',
       'marzo21','abril21', 'mayo21', #'junio20', 'julio20', 'agosto20', 'septiembre20',
       #'octubre20', 'noviembre20', 'diciembre20',
    ]]

############################################## lista de semanas 

listameses = [ 'febrero20', 'marzo20',
       'abril20', 'mayo20', 'junio20', 'julio20', 'agosto20', 'septiembre20',
       'octubre20', 'noviembre20', 'diciembre20', 'enero21', 'febrero21',
       'marzo21','abril21', 'mayo21', #'junio20', 'julio20', 'agosto20', 'septiembre20',
       #'octubre20', 'noviembre20', 'diciembre20',
    ]

#lista de las semanas 
fnameDict = listameses
names = list(fnameDict)




###############################
# TRATAMIENTO 
############################### Contagios  por día

endall = len(contagios)

#Select and sum all columns data
contagios1 = contagios.iloc[:,3:endall].sum()

# Make a DataFrame
contagios2 = pd.DataFrame(contagios1)

# index decesos 
contagios2['index'] = contagios2.index 
contagios2.rename(columns = {0:'cases', 'index':'days'}, inplace = True)


############################### Total de contagios 
contagiostotal = contagios2.cases.sum()
###############################


###############################   Contagios por mes  
# by months 

format = '%d-%m-%Y'
contagios2['days'] = pd.to_datetime(contagios2['days'], format=format)

# Filtering by years and months
cont_feb20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 2)]
cont_mar20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 3)]
cont_abr20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 4)]
cont_may20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 5)]
cont_jun20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 6)]
cont_jul20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 7)]
cont_ago20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 8)]
cont_sep20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 9)]
cont_oct20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 10)]
cont_nov20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 11)]
cont_dic20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 12)]
cont_ene21 = contagios2[(contagios2.days.dt.year == 2021 ) & (contagios2.days.dt.month == 1)]
cont_feb21 = contagios2[(contagios2.days.dt.year == 2021 ) & (contagios2.days.dt.month == 2)]
cont_mar21 = contagios2[(contagios2.days.dt.year == 2021 ) & (contagios2.days.dt.month == 3)]
cont_abr21 = contagios2[(contagios2.days.dt.year == 2021 ) & (contagios2.days.dt.month == 4)]
cont_may21 = contagios2[(contagios2.days.dt.year == 2021 ) & (contagios2.days.dt.month == 5)]
#cont_jun21 = contagios2[(contagios2.days.dt.year == 2021 ) & (contagios2.days.dt.month == 6)]
#cont_jul21 = contagios2[(contagios2.days.dt.year == 2021 ) & (contagios2.days.dt.month == 7)]
#cont_ago21 = contagios2[(contagios2.days.dt.year == 2021 ) & (contagios2.days.dt.month == 8)]
#cont_sep21 = contagios2[(contagios2.days.dt.year == 2021 ) & (contagios2.days.dt.month == 9)]
#cont_oct21 = contagios2[(contagios2.days.dt.year == 2021 ) & (contagios2.days.dt.month == 10)]
#cont_nov21 = contagios2[(contagios2.days.dt.year == 2021 ) & (contagios2.days.dt.month == 11)]
#cont_dic21 = contagios2[(contagios2.days.dt.year == 2021 ) & (contagios2.days.dt.month == 12)]

# Summarize by months 
contagios_feb20 = cont_feb20.cases.sum()
contagios_mar20 = cont_mar20.cases.sum()
contagios_abr20 = cont_abr20.cases.sum()
contagios_may20 = cont_may20.cases.sum()
contagios_jun20 = cont_jun20.cases.sum()
contagios_jul20 = cont_jul20.cases.sum()
contagios_ago20 = cont_ago20.cases.sum()
contagios_sep20 = cont_sep20.cases.sum()
contagios_oct20 = cont_oct20.cases.sum()
contagios_nov20 = cont_nov20.cases.sum()
contagios_dic20 = cont_dic20.cases.sum()
contagios_ene21 = cont_ene21.cases.sum()
contagios_feb21 = cont_feb21.cases.sum()
contagios_mar21 = cont_mar21.cases.sum()
contagios_abr21 = cont_abr21.cases.sum()
contagios_may21 = cont_may21.cases.sum()
#contagios_jun21 = cont_jun21.cases.sum()
#contagios_jul21 = cont_jul21.cases.sum()
#contagios_ago21 = cont_ago21.cases.sum()
#contagios_sep21 = cont_sep21.cases.sum()
#contagios_oct21 = cont_oct21.cases.sum()
#contagios_nov21 = cont_nov21.cases.sum()
#contagios_dic21 = cont_dic21.cases.sum()



#means
contagios_feb20_prom = round(cont_feb20.cases.mean())
contagios_mar20_prom = round(cont_mar20.cases.mean())
contagios_abr20_prom = round(cont_abr20.cases.mean())
contagios_may20_prom = round(cont_may20.cases.mean())
contagios_jun20_prom = round(cont_jun20.cases.mean())
contagios_jul20_prom = round(cont_jul20.cases.mean())
contagios_ago20_prom = round(cont_ago20.cases.mean())
contagios_sep20_prom = round(cont_sep20.cases.mean())
contagios_oct20_prom = round(cont_oct20.cases.mean())
contagios_nov20_prom = round(cont_nov20.cases.mean())
contagios_dic20_prom = round(cont_dic20.cases.mean())
contagios_ene21_prom = round(cont_ene21.cases.mean())
contagios_feb21_prom = round(cont_feb21.cases.mean())
contagios_mar21_prom = round(cont_mar21.cases.mean())
contagios_abr21_prom = round(cont_abr21.cases.mean())
contagios_may21_prom = round(cont_may21.cases.mean())
contagios_jun21_prom = round(cont_jun21.cases.mean())
contagios_jul21_prom = round(cont_jul21.cases.mean())
contagios_ago21_prom = round(cont_ago21.cases.mean())
contagios_sep21_prom = round(cont_sep21.cases.mean())
contagios_oct21_prom = round(cont_oct21.cases.mean())
contagios_nov21_prom = round(cont_nov21.cases.mean())
contagios_dic21_prom = round(cont_dic21.cases.mean())

##############################
# TRATAMIENTO 
############################### Contagios  por día

endall = len(decesos)

#Select and sum all columns data
decesos1 = contagios.iloc[:,3:endall].sum()

# Make a DataFrame
decesos2 = pd.DataFrame(decesos1)

# index decesos 
decesos2['index'] = decesos2.index 
decesos2.rename(columns = {0:'cases', 'index':'days'}, inplace = True)


############################### Total de contagios 
decesos_tot = decesos2.cases.sum()
###############################



format = '%d-%m-%Y'
decesos2['days'] = pd.to_datetime(decesos2['days'], format=format)
decesos2

dec_feb20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 2)]
dec_mar20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 3)]
dec_abr20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 4)]
dec_may20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 5)]
dec_jun20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 6)]
dec_jul20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 7)]
dec_ago20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 8)]
dec_sep20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 9)]
dec_oct20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 10)]
dec_nov20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 11)]
dec_dic20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 12)]
dec_ene21 = decesos2[(decesos2.days.dt.year == 2021 ) & (decesos2.days.dt.month == 1)]
dec_feb21 = decesos2[(decesos2.days.dt.year == 2021 ) & (decesos2.days.dt.month == 2)]
dec_mar21 = decesos2[(decesos2.days.dt.year == 2021 ) & (decesos2.days.dt.month == 3)]
dec_abr21 = decesos2[(decesos2.days.dt.year == 2021 ) & (decesos2.days.dt.month == 4)]
dec_may21 = decesos2[(decesos2.days.dt.year == 2021 ) & (decesos2.days.dt.month == 5)]
#dec_jun21 = decesos2[(decesos2.days.dt.year == 2021 ) & (decesos2.days.dt.month == 6)]
#dec_jul21 = decesos2[(decesos2.days.dt.year == 2021 ) & (decesos2.days.dt.month == 7)]
#dec_ago21 = decesos2[(decesos2.days.dt.year == 2021 ) & (decesos2.days.dt.month == 8)]
#dec_sep21 = decesos2[(decesos2.days.dt.year == 2021 ) & (decesos2.days.dt.month == 9)]
#dec_oct21 = decesos2[(decesos2.days.dt.year == 2021 ) & (decesos2.days.dt.month == 10)]
#dec_nov21 = decesos2[(decesos2.days.dt.year == 2021 ) & (decesos2.days.dt.month == 11)]
#dec_dic21 = decesos2[(decesos2.days.dt.year == 2021 ) & (decesos2.days.dt.month == 12)]


#sum
decesos_feb20 = dec_feb20.cases.sum()
decesos_mar20 = dec_mar20.cases.sum()
decesos_abr20 = dec_abr20.cases.sum()
decesos_may20 = dec_may20.cases.sum()
decesos_jun20 = dec_jun20.cases.sum()
decesos_jul20 = dec_jul20.cases.sum()
decesos_ago20 = dec_ago20.cases.sum()
decesos_sep20 = dec_sep20.cases.sum()
decesos_oct20 = dec_oct20.cases.sum()
decesos_nov20 = dec_nov20.cases.sum()
decesos_dic20 = dec_dic20.cases.sum()
decesos_ene21 = dec_ene21.cases.sum()
decesos_feb21 = dec_feb21.cases.sum()
decesos_mar21 = dec_mar21.cases.sum()
decesos_abr21 = dec_abr21.cases.sum()
decesos_may21 = dec_may21.cases.sum()
#decesos_jun21 = dec_jun21.cases.sum()
#decesos_jul21 = dec_jul21.cases.sum()
#decesos_ago21 = dec_ago21.cases.sum()
#decesos_sep21 = dec_sep21.cases.sum()
#decesos_oct21 = dec_oct21.cases.sum()
#decesos_nov21 = dec_nov21.cases.sum()
#decesos_dic21 = dec_dic21.cases.sum()


#means
#decesos_feb20_prom = round(dec_feb20.cases.mean()) 
decesos_mar20_prom = round(dec_mar20.cases.mean())
decesos_abr20_prom = round(dec_abr20.cases.mean())
decesos_may20_prom = round(dec_may20.cases.mean())
decesos_jun20_prom = round(dec_jun20.cases.mean())
decesos_jul20_prom = round(dec_jul20.cases.mean())
decesos_ago20_prom = round(dec_ago20.cases.mean())
decesos_sep20_prom = round(dec_sep20.cases.mean())
decesos_oct20_prom = round(dec_oct20.cases.mean())
decesos_nov20_prom = round(dec_nov20.cases.mean())
decesos_dic20_prom = round(dec_dic20.cases.mean())
decesos_ene21_prom = round(dec_ene21.cases.mean())
decesos_feb21_prom = round(dec_feb21.cases.mean())
decesos_mar21_prom = round(dec_mar21.cases.mean())
decesos_abr21_prom = round(dec_abr21.cases.mean())
decesos_may21_prom = round(dec_may21.cases.mean())
#decesos_jun21_prom = round(dec_jun21.cases.mean())
#decesos_jul21_prom = round(dec_jul21.cases.mean())
#decesos_ago21_prom = round(dec_ago21.cases.mean())
#decesos_sep21_prom = round(dec_sep21.cases.mean())
#decesos_oct21_prom = round(dec_oct21.cases.mean())
#decesos_nov21_prom = round(dec_nov21.cases.mean())
#decesos_dic21_prom = round(dec_dic21.cases.mean())



############################### contagios totales por estado

onlyc = contagios.iloc[:,3:]
contagios['total'] = onlyc.sum(1)
#create 'total' column
contagios['total']=contagios['total'].astype(int)
#merge base-contagios
cont= pd.merge(base,contagios, left_on= ["cve_ent_mun1"], right_on =["cve_ent"], how='inner')
#group by edos, sort and show
contaedos1 = pd.DataFrame(cont.groupby(['Nom_Ent'])['total','poblacion'].sum()).sort_values('total', ascending=False)
contaedos1.to_csv('0000proceso.csv')
contaedo = pd.read_csv('0000proceso.csv')
contaedos = contaedo.sort_values('total', ascending=True).tail(10)



############################### contagios (tasas) por estado 

contaedos1['tasa']=((contaedos1.total/contaedos1.poblacion)*100000).round(2)
contaedos2=contaedos1.sort_values('tasa', ascending=True)
contaedos2.to_csv('0000proceso.csv')
contaedo2a = pd.read_csv('0000proceso.csv')
contaedos2a = contaedo2a.sort_values('tasa', ascending=True).tail(10)

#para pie chart Contagios
contaedog = contaedo.stb.freq(['Nom_Ent'],value='total', thresh=60, other_label="Resto del país")




############################### decesos totales por estado

onlyd = decesos.iloc[:,3:]
decesos['total'] = onlyd.sum(1)
decesos['total']=decesos['total'].astype(int)
#merge
dec= pd.merge(base,decesos, left_on= ["cve_ent_mun1"], right_on =["cve_ent"], how='inner')
#group by edos
deceedos1 = pd.DataFrame(dec.groupby(['Nom_Ent'])['total','poblacion'].sum()).sort_values('total', ascending=False)
deceedos1.to_csv('0000proceso.csv')
deceedo = pd.read_csv('0000proceso.csv')
deceedos = deceedo.sort_values('total', ascending=True).tail(10)
####### W19.18022021 


############################### decesos (tasas) por estado

deceedos1['tasa']=((deceedos1.total/deceedos1.poblacion)*100000).round(2)
deceedos2= deceedos1.sort_values('tasa', ascending=True).tail(10)
deceedos2.to_csv('0000proceso.csv')
deceedos2a = pd.read_csv('0000proceso.csv')

#para pie chart Decesos
deceedosg = deceedos.stb.freq(['Nom_Ent'],value='total', thresh=60, other_label="Resto del país")


############################### Total  activos

#  ACTIVOS CONFIRMADOS
cols5=len(contagios.columns)
actv=cols5-15
contagios['act_conf']= contagios.iloc[:,actv:cols5].sum(axis=1)
act_confirmados=contagios['act_conf'].sum()

#  ACTIVOS DEFUNCIONES
cols6=len(decesos.columns)
actv1=cols6-15
decesos['act_def']=decesos.iloc[:,actv1:cols6].sum(axis=1)
act_defunciones=decesos['act_def'].sum()

activos_tot= act_confirmados+act_defunciones


############################### Suma y porcentaje de 60+

muertos60_mas.drop('cve_geo1', 1, inplace=True)
muertos60_mas = muertos60_mas.drop([0])
muertos60_mas.decesos_60_y_mas=muertos60_mas.decesos_60_y_mas.astype(int)
tot_60=muertos60_mas.decesos_60_y_mas.sum()
tot_60_p=((tot_60*100)/decesos_tot).round(1)

############################### Suma y porcentaje de 3 mayores comorbilidades

pasa.drop('Unnamed: 0',1,inplace=True)
deseases_tot=pasa.sum().sort_values(ascending=False).sum()
deseases_3=pasa.sum().sort_values(ascending=False).head(3).sum()
deseases_3_p=((deseases_3*100)/deseases_tot).round(2)






#############################################
# G R A F I C A S 
############################################# Grafica1

figaro = go.Figure()
figaro.add_trace(go.Bar(x=contagios2['days'],y=contagios2['cases'],
                marker_color='indianred'  # cambiar nuemeritos de rgb
                ))
figaro.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='',
    xaxis_tickfont_size= 6,
    yaxis=dict(
        title='Decesos diarios',
        titlefont_size=14,
        tickfont_size=12),
    font_family= "Rockwell")
#figaro.add_shape( # add a horizontal "target" line
#    type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot",
#    x0=0, x1=1, xref="paper", y0=4500, y1=4500, yref="y"
#)
#
#figaro.add_annotation(x=20000, y="11-01-2021",
#           text="Text annotation without arrow",
#            showarrow=False,
#            yshift=10)
#
    #autosize=False,
    #width=1000,
    #height=400
    

############################################ Grafica 2

figaro2 = go.Figure()
figaro2.add_trace(go.Bar(x=decesos2['days'],y=decesos2['cases'],
                marker_color='slategray'  # cambiar nuemeritos de rgb
               ))
figaro2.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='',
    xaxis_tickfont_size= 6,
    yaxis=dict(
        title='Decesos diarios',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"),
    #autosize=False,
    #width=1000,
    #height=400
    )


###################################################Tabla meses
patabla6 = {
            'Feb20'     : [str(f"{contagios_feb20:,d}")],#, decesos_feb20],
            'Mar20'     : [str(f"{contagios_mar20:,d}")],#, decesos_mar20],
            'Abr20'     : [str(f"{contagios_abr20:,d}")],#, decesos_abr20],
            'May20'     : [str(f"{contagios_may20:,d}")],#, decesos_may20],
            'Jun20'     : [str(f"{contagios_jun20:,d}")],#, decesos_jun20],
            'Jul20'     : [str(f"{contagios_jul20:,d}")],#, decesos_jul20],
            'Ago20'     : [str(f"{contagios_ago20:,d}")],#, decesos_ago20],
            'Sept20'    : [str(f"{contagios_sep20:,d}")],#, decesos_sep20],
            'Oct20'     : [str(f"{contagios_oct20:,d}")],#, decesos_oct20],
            'Nov20'     : [str(f"{contagios_nov20:,d}")],#, decesos_nov20],
            'Dic20'     : [str(f"{contagios_dic20:,d}")],#, decesos_dic20],
            'Ene21'     : [str(f"{contagios_ene21:,d}")],#, decesos_ene21],
            'Feb21'     : [str(f"{contagios_feb21:,d}")],#, decesos_feb21],
            'Mar21'     : [str(f"{contagios_mar21:,d}")],#, decesos_feb21],
            'Abr21'     : [str(f"{contagios_abr21:,d}")],#, decesos_abr20],
            'May21'     : [str(f"{contagios_may21:,d}")],#, decesos_may20],
           # 'Jun21'     : [str(f"{contagios_jun21:,d}")],#, decesos_jun20],
           # 'Jul21'     : [str(f"{contagios_jul21:,d}")],#, decesos_jul20],
           # 'Ago21'     : [str(f"{contagios_ago21:,d}")],#, decesos_ago20],
           # 'Sept21'    : [str(f"{contagios_sep21:,d}")],#, decesos_sep20],
           # 'Oct21'     : [str(f"{contagios_oct21:,d}")],#, decesos_oct20],
           # 'Nov21'     : [str(f"{contagios_nov21:,d}")],#, decesos_nov20],
           # 'Dic21'     : [str(f"{contagios_dic21:,d}")],#, decesos_dic20],

                            }


patabla7 = pd.DataFrame (patabla6, columns = [
                                              'Feb20','Mar20','Abr20','May20','Jun20',
    'Jul20','Ago20','Sept20','Oct20','Nov20','Dic20',
    'Ene21','Feb21', 'Mar21','Abr21','May21',#'Jun21',
   # 'Jul21','Ago21','Sept21','Oct21','Nov21','Dic21',
])

################################################################Cintillo mensual decesos
patabla6a = {
            'Feb20'   : [str(f"{decesos_feb20:,d}")],#, decesos_feb20],
            'Mar20'   : [str(f"{decesos_mar20:,d}")],#, decesos_mar20],
            'Abr20'   : [str(f"{decesos_abr20:,d}")],#, decesos_abr20],
            'May20'   : [str(f"{decesos_may20:,d}")],#, decesos_may20],
            'Jun20'   : [str(f"{decesos_jun20:,d}")],#, decesos_jun20],
            'Jul20'   : [str(f"{decesos_jul20:,d}")],#, decesos_jul20],
            'Ago20'   : [str(f"{decesos_ago20:,d}")],#, decesos_ago20],
            'Sept20'  : [str(f"{decesos_sep20:,d}")],#, decesos_sep20],
            'Oct20'   : [str(f"{decesos_oct20:,d}")],#, decesos_oct20],
            'Nov20'   : [str(f"{decesos_nov20:,d}")],#, decesos_nov20],
            'Dic20'   : [str(f"{decesos_dic20:,d}")],#, decesos_dic20],
            'Ene21'   : [str(f"{decesos_ene21:,d}")],#, decesos_ene21],
            'Feb21'   : [str(f"{decesos_feb21:,d}")],#, decesos_feb21],
            'Mar21'   : [str(f"{decesos_mar21:,d}")],#, decesos_mar21],
            'Abr21'   : [str(f"{decesos_abr21:,d}")],#, decesos_abr20],
            'May21'   : [str(f"{decesos_may21:,d}")],#, decesos_may20],
           # 'Jun21'   : [str(f"{decesos_jun21:,d}")],#, decesos_jun20],
           # 'Jul21'   : [str(f"{decesos_jul21:,d}")],#, decesos_jul20],
           # 'Ago21'   : [str(f"{decesos_ago21:,d}")],#, decesos_ago20],
           # 'Sept21'  : [str(f"{decesos_sep21:,d}")],#, decesos_sep20],
           # 'Oct21'   : [str(f"{decesos_oct21:,d}")],#, decesos_oct20],
           # 'Nov21'   : [str(f"{decesos_nov21:,d}")],#, decesos_nov20],
           # 'Dic21'   : [str(f"{decesos_dic21:,d}")],#, decesos_dic20],

                            }

patabla7a = pd.DataFrame (patabla6a, columns = [
                                              'Feb20','Mar20','Abr20','May20','Jun20',
    'Jul20','Ago20','Sept20','Oct20','Nov20','Dic20',
   'Ene21','Feb21', 'Mar21','Abr21','May21',#'Jun21',
   # 'Jul21','Ago21','Sept21','Oct21','Nov21','Dic21',
])

########################################################### Graficas barras
# 1 Contagios
g10edosc = go.Figure()
g10edosc.add_trace(go.Bar(x=contaedos['total'],y=contaedos['Nom_Ent'],
                          orientation='h',
                #name='Contagios confirmados COVID-19',
                          marker_color='firebrick',
                          #align= 'center',

                         ))
g10edosc.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    #xaxis_tickangle=-45,
    template = 'simple_white',
    title='Contagios',
    title_font_family= 'Montserrat Medium',
    title_font_color= 'lightpink',
    title_font_size= 18,
    xaxis_tickfont_size= 12,
    yaxis=dict(
        titlefont_size=80,
        tickfont_size= 12,
        titlefont_family= 'Monserrat ExtraBold',
        title_font_color= "white"
        ))

########################################################  2 Tasa Contagios
g10edosct = go.Figure()
g10edosct.add_trace(go.Bar(x=contaedos2a['tasa'],y=contaedos2a['Nom_Ent'],
                          orientation='h',
                          marker_color='palevioletred',
                         ))
g10edosct.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='Tasa Contagios',
    title_font_family= 'Montserrat Medium',
    title_font_color= 'lightpink',
    title_font_size= 18,
    xaxis_tickfont_size= 3,
    yaxis=dict(
        titlefont_size=80,
        tickfont_size= 10,
        titlefont_family= 'Monserrat ExtraBold',
        ))



############################################################ 3 Decesos
g10edosd = go.Figure()
g10edosd.add_trace(go.Bar(x=deceedos['total'],y=contaedos['Nom_Ent'],
                #name='Contagios confirmados COVID-19',
                marker_color='gray',
                orientation='h'          
                # cambiar nuemeritos de rgb
                ))

g10edosd.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='Decesos',
    uniformtext_minsize=10,
    uniformtext_mode='hide',
    title_font_family= 'Montserrat Medium',
    title_font_color= 'lightgray',
    title_font_size= 18,
    xaxis_tickfont_size= 3,
    yaxis=dict(
        titlefont_size=80,
        tickfont_size= 10,
        titlefont_family= 'Montserrat ExtraBold',
        ))

############################################################ 4 Tasa de Letalidad
g10edosdt = go.Figure()
g10edosdt.add_trace(go.Bar(x=deceedos2a['tasa'],y=contaedos2a['Nom_Ent'],
                #name='Contagios confirmados COVID-19',
                marker_color='slategray',
                orientation='h'          
                
                ))
g10edosdt.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_mode='hide',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='Tasa de Decesos',
    title_font_family= 'Montserrat Medium',
    title_font_color= 'lightgray',
    title_font_size= 18,
    xaxis_tickfont_size= 3,
    yaxis=dict(
        titlefont_size=80,
        tickfont_size= 10,
        titlefont_family= 'Montserrat ExtraBold',
         #autosize=True,
   
   
        ))



############################### Gráfica PIE de Contagios por estado

piec = px.pie(contaedog, values='total', names='Nom_Ent',
             color_discrete_sequence=px.colors.sequential.Reds, hole=.5
              ,
             #title='Distribución de contagios',
             )
piec.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  uniformtext_minsize=10,
                  uniformtext_mode='hide',
                  autosize=True,
                  width= 550,
                  height=550,
                  title_font_size = 12,
                  font_color="gray",
                  title_font_color="firebrick",
                  )


############################### Gráfica Pie de Deceso por estado

pied = px.pie(deceedosg, values='total', names='Nom_Ent',
             color_discrete_sequence=px.colors.sequential.Greys, hole=.4,
             #title='      Decesos',
             #titlefont_size = 15,
             #font_family = 'Monserrat ExtraBold'
              
             )

pied.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  uniformtext_minsize=12,
                  uniformtext_mode='hide',
                  #font_family= "Monserrat",
                  autosize=True,
                  width= 425,
                  height=400,
                  title_font_size = 15,
                  font_color="gray",
                  title_font_color="black",
                  #title_font_family = 'Monserrat ExtraBold' 
                   )

########################################## MAPA







####################################

# A P 
####################################

########### Define your variables
mytitle=' '
tabtitle='COVID-19 en México'
sourceurl='https://datos.covid-19.conacyt.mx/'


server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. LUX], server=server)

body = html.Div([
    
       html.Hr(),
       html.Br(),
       html.Br(),
    
        dbc.Row(
            [
           
           dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/CamaraDiputados/blob/main/application/static/logocamara.jfif?raw=true"),
                        width=2, lg={'size': 1,  "offset": 1, }),
            
#           dbc.Col(html.H6(" S e c r e t a r í a   G e n e r a l," 
#                           " Secretaría de Servicios Parlamentarios, "
#                           " México, 2021 "),
#                  width={'size': 3, 'offset': 0}),
#               ], justify="start",),

# Title
        #dbc.Row(
           #[
            dbc.Col(html.H1("COVID-19 en México"),
                  width={'size' : 7,
                         'offset' : 3, 
                         'color' : 'danger'
                        }), 
                

            ],justify="start"),

    
# Fecha de actualización
    
       dbc.Row(
           [dbc.Col(html.H6([str(d2), ",  Fuente: Secretaría de Salud"]),
               width={'size' : "auto",
                      'offset' : 4,
            }), 
            ]),
    
       html.Hr(),

    
#################################### Franja ACTIVOS
#     dbc.Row(
#           [dbc.Col(html.H4("Activos"),
#                  width={'size' : "auto",'offset' : 1}),]),
#     dbc.Row(
#           [
#            dbc.Col(html.H2([str(f"{activos_tot:,d}")]),
#               width={'size' : "auto",'offset' : 1, 'colors' : 'danger'}), 
#               
#               ]),#

    
#################################### Franja CONTAGIOS   
#Contagios 
       # Suma total de contagios    
     dbc.Row(
           [dbc.Col(html.H3("Contagios"),
                  width={'size' : "auto",'offset' : 1}),]),
     dbc.Row(
           [
            dbc.Col(html.H2([str(f"{contagiostotal:,d}")]),
               width={'size' : "auto",'offset' : 1, 'colors' : 'danger'}), 
               ]),
           
       # Grafica de contagios    
       dbc.Row([dbc.Col(dcc.Graph(figure=figaro, config= "autosize"))]),
       
       dbc.Row(
           [
               dbc.Col(html.H5("Contagios acumulados por mes"),
                      width={'size' : "auto",'offset' : 1,}), 
           ]
           ),
           
       # Tabla de contagios mensuales
       dbc.Row(
           [
               dbc.Col(dbc.Table.from_dataframe(patabla7, 
                       striped=True), 
                      width={'size' : 10,'offset' : 0,}), 
#               width=10, sm={'size':auto, 'offset':1,},
                      
          ]),
    
       html.Hr(), 

    
#################################### Franja DECESOS    
#Decesos 

       # Suma total de Decesos    
       dbc.Row(
           [
            dbc.Col(html.H3("Decesos"),
                  width={'size' : "auto",'offset' : 1,'colors' : 'light'}),]),
    
       dbc.Row(
           [
            dbc.Col(html.H2([str(f"{decesos_tot:,d}")]),
               width={'size' : "auto",'offset' : 1,}), 
               ]),

     #################################### Franja 60+

     dbc.Row(
           [dbc.Col(html.H5("Con más de 60 años:"),
                  width={'size' : "auto",'offset' : 1}),]),
     dbc.Row(
           [
            dbc.Col(html.H5(#[str(f"{tot_60:,d}"), 
                             [str(tot_60_p), "%"]),
               width={'size' : "auto",'offset' : 1, 'colors' : 'danger'}), 
               ]),

 
        
       # Grafica de decesos    
       dbc.Row([dbc.Col(dcc.Graph(figure=figaro2, config= "autosize"))]),

       dbc.Row(
           [
               dbc.Col(html.H5("Decesos acumulados por mes"),
                      width={'size' : "auto",'offset' : 1,}), 
           ]
           ),
       # Tabla de decesos mensuales
       dbc.Row(
           [
               dbc.Col(dbc.Table.from_dataframe(patabla7a, 
                       striped=True), 
                      width={'size' : 10,'offset' : 0,}), 
           #    width=10, sm={'size':10, 'offset':0,},
          ]),
    
       html.Hr(),
       html.Hr(),

    
#################################### Franja Los RANKINGS    
# los rankings 
    
       dbc.Row([dbc.Col(html.H3('Las 10 entidades con más... '),
                   width={'size' : "auto",'offset' : 1,}, 
               )]),         

       dbc.Row(
           [
           dbc.Col(html.Div(dcc.Graph(figure=g10edosc, 
                               style={"size":0,
                                          }))), 
       
           dbc.Col(html.Div(dcc.Graph(figure=g10edosct,
                                style={"size":3,
                                          }))),

           dbc.Col(html.Div(dcc.Graph(figure=g10edosd, 
                                style={"size":6
                                          }))),

           dbc.Col(html.Div(dcc.Graph(figure=g10edosdt,
                                style={"size":9
                                          }))),
           ]),
    
       html.Hr(),

 #################################### Franja Los PIES    
# Distribución de contagios y decesos 
   
    
       dbc.Row(
           [
           dbc.Col(html.H3('Alrededor de 60% de casos se concentran en... '),
                   width={'size' : "auto",'offset' : 1,}),
           ]),
                
       dbc.Row(
           [
           dbc.Col(html.H5("Contagios"),
                   width={'size' : "auto",'offset' : 1,}),
               
           dbc.Col(html.H5("Decesos"),
                   width={'size' : "auto",'offset' : 6,}),

           ]),     

       dbc.Row([
           dbc.Col(dcc.Graph(figure=piec),
                                width=6,  md={"size":5,
                                        "offset": 0
                                          }),

           dbc.Col(dcc.Graph(figure=pied),
                                width=5, md={"size":4,
                                        "offset": 0, 
                                        
                                          }),
           ]),
    
       html.Hr(),
       html.Hr(),

   
   
#insertar en app al final de aquí.... 
    
           dbc.Col(html.H1("Acumulados mensuales por entidad"), 
                width={'size' : "auto",'offset' : 1 }),
                #style={'text-align': 'left'}
    
    
           dbc.Col(dcc.Dropdown(
           id="slct_year",
           options=[{'label':name, 'value':name}
                 for name in names],
           value = list(fnameDict)[0]),
                width={'size' : 6,'offset' : 1 },
                  style={'text-size': 28}),


        #style={'width': '70%', 'display': 'inline-block'},
        #),
       html.Div(id='output_container', children=[]),
       html.Br(),
        
           dcc.Graph(id='my_bee_map', figure={},
                      style={'width': '100%', 'display': 'inline-block',
                            'align': 'center'}),
    
       html.Br(),
       html.Br(),
       html.Br(),
       html.Br(),
    
        dbc.Row([
           
           dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/CamaraDiputados/blob/main/application/static/logocamara.jfif?raw=true"),
                        width=4, lg={'size': 1,  "offset": 3, }),
            
           dbc.Col(html.H6(" S e c r e t a r í a   G e n e r a l," 
                           " Secretaría de Servicios Parlamentarios, "
                           " México, 2021 "),
                  width={'size': 3, 'offset': 0}),
               ], justify="start",),
      dbc.Row([    
           dbc.Col(html.H5([dbc.Badge("Equipo responsable", 
                          href="https://raw.githubusercontent.com/fdealbam/feminicidios/main/Autores.pdf",
                          #color="light",
                          #className="ml-1")
                                     )]),
                  width={'size': 3,  "offset": 4}),
                       ], justify="start",),
        
            ])
        
        # -----------------------------------
        # Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
    Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
    )
def update_graph(option_slctd):
    
    print(option_slctd)
    print(type(option_slctd))
        
    container = "Mes seleccionado: {}".format(option_slctd)
        
        
    semnalgraph =  px.choropleth_mapbox(concat2[(option_slctd)],
                                   geojson=geo_df.geometry,
                                   locations=concat2.index,
                                   color= (option_slctd),
                                   range_color=[100, 1500],     
                                   center={"lat": 23.88234, "lon": -102.28259},
                                   mapbox_style="carto-positron",
                                   zoom= 4.5,
                                   opacity=.6,
                                   color_continuous_scale=px.colors.sequential.Oranges,
      
                                       )     

    
    semnalgraph.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0},
        autosize=False,
        width=1200,
        height=700,
        showlegend = False
            )
    
    return container, semnalgraph
        
  
  
  
  
  
  
#])

app.layout = html.Div([body])

from application.dash import app
from settings import config

if __name__ == "__main__":
    app.run_server()
    
    
    
    
#https://plotly.com/python/builtin-colorscales/
