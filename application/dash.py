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


os.chdir(r"C:\Users\PRIME\AnacondaProjects\Project_curso\\")
pd.read_csv("Municipal-Delitos-2015-2021_ene2021.csv")
columns = ['Año', 'Clave_Ent', 'Entidad', 'Cve. Municipio', 'Municipio',
        'Tipo de delito',  'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
       'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

delitos = pd.read_csv("Municipal-Delitos-2015-2021_ene2021.csv", encoding= "Latin-1", usecols= columns)

delitos.groupby(['Año','Entidad','Tipo de delito'])['Enero', 
                 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
       'Julio', 'Agosto', 'Septiembre', 'Octubre',
       'Noviembre', 'Diciembre'].sum().to_csv("00.csv",  header=True)

feminicidio= pd.read_csv("00.csv")
feminicidio[feminicidio["Tipo de delito"]== "Feminicidio"].to_csv("01.csv", header=True)

fem= pd.read_csv("01.csv")


############################################### separación de años

year15= fem[fem.Año == 2015]
year16= fem[fem.Año == 2016]
year17= fem[fem.Año == 2017]
year18= fem[fem.Año == 2018]
year19= fem[fem.Año == 2019]
year20= fem[fem.Año == 2020]

############################################### Agregar suffix de años

y15 = year15.add_suffix('15')
y15.rename(columns ={'Año15': 'Año', 'Tipo de delito15': 'Tipo de delito', 'Unnamed: 015' : 'Unnamed: 0',
                            'Entidad15': 'Entidad'}, inplace = True)

y16 = year16.add_suffix('16')
y16.rename(columns ={'Año16': 'Año', 'Tipo de delito16': 'Tipo de delito', 'Unnamed: 016' : 'Unnamed: 0',
                            'Entidad16': 'Entidad'}, inplace = True)

y17 = year17.add_suffix('17')
y17.rename(columns ={'Año17': 'Año', 'Tipo de delito17': 'Tipo de delito', 'Unnamed: 017' : 'Unnamed: 0',
                            'Entidad17': 'Entidad'}, inplace = True)

y18= year18.add_suffix('18')
y18.rename(columns ={'Año18': 'Año', 'Tipo de delito18': 'Tipo de delito','Unnamed: 018' : 'Unnamed: 0',
                            'Entidad18': 'Entidad'}, inplace = True)

y19= year19.add_suffix('19')
y19.rename(columns ={'Año19': 'Año', 'Tipo de delito19': 'Tipo de delito', 'Unnamed: 019' : 'Unnamed: 0',
                            'Entidad19': 'Entidad'}, inplace = True)

y20= year20.add_suffix('20')
y20.rename(columns ={'Año20': 'Año', 'Tipo de delito20': 'Tipo de delito','Unnamed: 020' : 'Unnamed: 0',
                            'Entidad20': 'Entidad'}, inplace = True)



############################################### Concat todos los años

fa = y15.merge(y16, on="Entidad",  how="inner")
fb = fa.merge(y17, on="Entidad",  how="inner")
fc = fb.merge(y18, on="Entidad",  how="inner")
fd = fc.merge(y19, on="Entidad",  how="inner")
fe = fd.merge(y20, on="Entidad",  how="inner")
                      
femi15_20 = fe[[
 'Entidad',
 'Enero15',
 'Febrero15',
 'Marzo15',
 'Abril15',
 'Mayo15',
 'Junio15',
 'Julio15',
 'Agosto15',
 'Septiembre15',
 'Octubre15',
 'Noviembre15',
 'Diciembre15',
 
 'Enero16',
 'Febrero16',
 'Marzo16',
 'Abril16',
 'Mayo16',
 'Junio16',
 'Julio16',
 'Agosto16',
 'Septiembre16',
 'Octubre16',
 'Noviembre16',
 'Diciembre16',

 'Enero17',
 'Febrero17',
 'Marzo17',
 'Abril17',
 'Mayo17',
 'Junio17',
 'Julio17',
 'Agosto17',
 'Septiembre17',
 'Octubre17',
 'Noviembre17',
 'Diciembre17',
 'Enero18',
 'Febrero18',
 'Marzo18',
 'Abril18',
 'Mayo18',
 'Junio18',
 'Julio18',
 'Agosto18',
 'Septiembre18',
 'Octubre18',
 'Noviembre18',
 'Diciembre18',
 
 'Enero19',
 'Febrero19',
 'Marzo19',
 'Abril19',
 'Mayo19',
 'Junio19',
 'Julio19',
 'Agosto19',
 'Septiembre19',
 'Octubre19',
 'Noviembre19',
 'Diciembre19',

 'Enero20',
 'Febrero20',
 'Marzo20',
 'Abril20',
 'Mayo20',
 'Junio20',
 'Julio20',
 'Agosto20',
 'Septiembre20',
 'Octubre20',
 'Noviembre20',
 'Diciembre20']]

##CRear columna de TOTAL ANUAL 
femi15_20['Total2015']= femi15_20[[ 'Enero15', 'Febrero15', 'Marzo15', 'Abril15', 'Mayo15',
                               'Junio15', 'Julio15', 'Agosto15', 'Septiembre15', 'Octubre15',
                               'Noviembre15', 'Diciembre15',]].sum(axis=1)
femi15_20['Total2016']= femi15_20[[ 'Enero16', 'Febrero16', 'Marzo16', 'Abril16', 'Mayo16',
                               'Junio16', 'Julio16', 'Agosto16', 'Septiembre16', 'Octubre16',
                               'Noviembre16', 'Diciembre16',]].sum(axis=1)
femi15_20['Total2017']= femi15_20[[ 'Enero17', 'Febrero17', 'Marzo17', 'Abril17', 'Mayo17',
                               'Junio17', 'Julio17', 'Agosto17', 'Septiembre17', 'Octubre17',
                               'Noviembre17', 'Diciembre17',]].sum(axis=1)
femi15_20['Total2018']= femi15_20[[ 'Enero18', 'Febrero18', 'Marzo18', 'Abril18', 'Mayo18',
                               'Junio18', 'Julio18', 'Agosto18', 'Septiembre18', 'Octubre18',
                               'Noviembre18', 'Diciembre18',]].sum(axis=1)
femi15_20['Total2019']= femi15_20[[ 'Enero19', 'Febrero19', 'Marzo19', 'Abril19', 'Mayo19',
                               'Junio19', 'Julio19', 'Agosto19', 'Septiembre19', 'Octubre19',
                               'Noviembre19', 'Diciembre19',]].sum(axis=1)
femi15_20['Total2020']= femi15_20[[ 'Enero20', 'Febrero20', 'Marzo20', 'Abril20', 'Mayo20',
                               'Junio20', 'Julio20', 'Agosto20', 'Septiembre20', 'Octubre20',
                               'Noviembre20', 'Diciembre20',]].sum(axis=1)


#identificadores
conf_2015= femi15_20.Total2015.sum()
conf_2016= femi15_20.Total2016.sum()
conf_2017= femi15_20.Total2017.sum()
conf_2018= femi15_20.Total2018.sum()
conf_2019= femi15_20.Total2019.sum()
conf_2020= femi15_20.Total2020.sum()


#--------------------------- PREPARA GRAFICA MENSUAL
pagra = fe[[
  'Enero15', 'Febrero15', 'Marzo15', 'Abril15', 'Mayo15', 'Junio15', 'Julio15', 'Agosto15', 
    'Septiembre15', 'Octubre15', 'Noviembre15', 'Diciembre15',
 
 'Enero16', 'Febrero16', 'Marzo16', 'Abril16', 'Mayo16', 'Junio16', 'Julio16', 'Agosto16', 
    'Septiembre16', 'Octubre16', 'Noviembre16', 'Diciembre16',

 'Enero17', 'Febrero17', 'Marzo17', 'Abril17', 'Mayo17', 'Junio17', 'Julio17', 'Agosto17', 
    'Septiembre17', 'Octubre17', 'Noviembre17', 'Diciembre17', 
    'Enero18', 'Febrero18', 'Marzo18',    'Abril18', 'Mayo18', 'Junio18', 'Julio18', 'Agosto18',
    'Septiembre18', 'Octubre18', 'Noviembre18', 'Diciembre18',
 
 'Enero19', 'Febrero19', 'Marzo19', 'Abril19', 'Mayo19', 'Junio19', 'Julio19', 'Agosto19', 
    'Septiembre19', 'Octubre19', 'Noviembre19', 'Diciembre19',

 'Enero20', 'Febrero20', 'Marzo20', 'Abril20', 'Mayo20', 'Junio20', 'Julio20', 'Agosto20',
    'Septiembre20','Octubre20', 'Noviembre20', 'Diciembre20']]


pagrafm = pagra.stb.subtotal()
pagrafm.to_csv("0000procesod.csv")
#Selecciona ultima columna (Totales)
other  = pd.read_csv('0000procesod.csv')
other_s = other.iloc[32]
other_b = pd.DataFrame(other_s)
other_b.to_csv('0000procesodi.csv')
vuelve_a_abrir = pd.read_csv('0000procesodi.csv')
##Elimina filas 0 a 4 
gra_mes = vuelve_a_abrir.drop([0])
#Renombra titulo de columna
gra_mes = gra_mes.rename(columns= {"Unnamed: 0": "Mes"})
gra_mes = gra_mes.rename(columns= {"32": "Total"})
gra_mes['Total'] = pd.to_numeric(gra_mes['Total'])

graf_meses = go.Figure()
graf_meses.add_trace(go.Bar(x=pruebad['Mes'],y=pruebad['Total'],
                marker_color='indianred'  # cambiar nuemeritos de rgb
                ))
graf_meses.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='',
    xaxis_tickfont_size= 6,
    yaxis=dict(
        title='Acumulados mensuales',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"),
    #autosize=False,
    #width=1000,
    #height=400
    )
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
concat0 = geo_df.merge(femi15_20, left_on= "name", right_on= "Entidad", how= "right")



# Selección de columnas 
concat2 = concat0[[
 'geometry', 'name',
 'Entidad',
 'Enero15',
 'Febrero15',
 'Marzo15',
 'Abril15',
 'Mayo15',
 'Junio15',
 'Julio15',
 'Agosto15',
 'Septiembre15',
 'Octubre15',
 'Noviembre15',
 'Diciembre15',
 'Enero16',
 'Febrero16',
 'Marzo16',
 'Abril16',
 'Mayo16',
 'Junio16',
 'Julio16',
 'Agosto16',
 'Septiembre16',
 'Octubre16',
 'Noviembre16',
 'Diciembre16',
 'Enero17',
 'Febrero17',
 'Marzo17',
 'Abril17',
 'Mayo17',
 'Junio17',
 'Julio17',
 'Agosto17',
 'Septiembre17',
 'Octubre17',
 'Noviembre17',
 'Diciembre17',
 'Enero18',
 'Febrero18',
 'Marzo18',
 'Abril18',
 'Mayo18',
 'Junio18',
 'Julio18',
 'Agosto18',
 'Septiembre18',
 'Octubre18',
 'Noviembre18',
 'Diciembre18',
 'Enero19',
 'Febrero19',
 'Marzo19',
 'Abril19',
 'Mayo19',
 'Junio19',
 'Julio19',
 'Agosto19',
 'Septiembre19',
 'Octubre19',
 'Noviembre19',
 'Diciembre19',
 'Enero20',
 'Febrero20',
 'Marzo20',
 'Abril20',
 'Mayo20',
 'Junio20',
 'Julio20',
 'Agosto20',
 'Septiembre20',
 'Octubre20',
 'Noviembre20',
 'Diciembre20',
 'Total2015',
 'Total2016',
 'Total2017',
 'Total2018',
 'Total2019',
 'Total2020']]





#########################################################

# M A P A S

######################################################### MAPAS ANUALES

# 2015

mapa2015 =  px.choropleth_mapbox(concat2,
                                   geojson=geo_df.geometry,
                                   locations=concat2.index,
                                   color= "Total2015",   
                                   center={"lat": 23.88234, "lon": -102.28259},
                                   mapbox_style="white-bg",
                                   zoom= 2,
                                   opacity=.6,
                                   color_continuous_scale=px.colors.sequential.Reds,
                                       ) 
mapa2015.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    height=200, width = 200, margin={"r":0,"t":0,"l":0,"b":0},
                      coloraxis_showscale=False)


# 2016

mapa2016 =  px.choropleth_mapbox(concat2,
                                   geojson=geo_df.geometry,
                                   locations=concat2.index,
                                   color= "Total2016",   
                                   center={"lat": 23.88234, "lon": -102.28259},
                                   mapbox_style="white-bg",
                                   zoom= 2,
                                   opacity=.6,
                                   color_continuous_scale=px.colors.sequential.Reds,
      
                                       ) 
mapa2016.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    height=200, width = 200, margin={"r":0,"t":0,"l":0,"b":0},
                      coloraxis_showscale=False)


# 2017

mapa2017 =  px.choropleth_mapbox(concat2,
                                   geojson=geo_df.geometry,
                                   locations=concat2.index,
                                   color= "Total2017",   
                                   center={"lat": 23.88234, "lon": -102.28259},
                                   mapbox_style="white-bg",
                                   zoom= 2,
                                   opacity=.6,
                                   color_continuous_scale=px.colors.sequential.Reds,
      
                                       ) 
mapa2017.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    height=200, width = 200, margin={"r":0,"t":0,"l":0,"b":0},
                      coloraxis_showscale=False)


# 2018

mapa2018 =  px.choropleth_mapbox(concat2,
                                   geojson=geo_df.geometry,
                                   locations=concat2.index,
                                   color= "Total2018",   
                                   center={"lat": 23.88234, "lon": -102.28259},
                                   mapbox_style="white-bg",
                                   zoom= 2,
                                   opacity=.6,
                                   
                                   color_continuous_scale=px.colors.sequential.Reds,
      
                                       ) 
mapa2018.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    height=200, width = 200, margin={"r":0,"t":0,"l":0,"b":0},
                      coloraxis_showscale=False)


# 2019

mapa2019 =  px.choropleth_mapbox(concat2,
                                   geojson=geo_df.geometry,
                                   locations=concat2.index,
                                   color= "Total2019",   
                                   center={"lat": 23.88234, "lon": -102.28259},
                                   mapbox_style="white-bg",
                                   zoom= 2,
                                   opacity=.6,
                                   color_continuous_scale=px.colors.sequential.Reds,
      
                                       )
mapa2019.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    height=200, width = 200, margin={"r":0,"t":0,"l":0,"b":0},
                      coloraxis_showscale=False)


# 2020

mapa2020 =  px.choropleth_mapbox(concat2,
                                   geojson=geo_df.geometry,
                                   locations=concat2.index,
                                   color= "Total2020",   
                                   center={"lat": 23.88234, "lon": -102.28259},
                                   mapbox_style="white-bg",
                                   zoom= 2,
                                   opacity=.6,  
                                   labels = None,
                                   color_continuous_scale=px.colors.sequential.Reds,
      
                                       ) 
mapa2020.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    template = 'simple_white',
    
    height=200, width = 200, margin={"r":0,"t":0,"l":0,"b":0},
                       coloraxis_showscale=False)



###########################
# FALTA UNA GRAFICA 
#######################













####################################

# A P P

####################################

########### Define your variables
mytitle=' '
tabtitle='Feminicidios'
sourceurl='https://www.gob.mx/sesnsp/acciones-y-programas/datos-abiertos-de-incidencia-delictiva?state=published'


server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. LUX], server=server)

body = html.Div([
    
       html.Hr(),

# Cintillo 000
        dbc.Row(
           [
               dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/CamaraDiputados/blob/main/application/static/logocamara.jfif?raw=true"),
                        width={'size': 1,  "offset": 1}),
               dbc.Col(html.H1("Feminicidios en México"),
                        width={'offset' : 2}),
               #dbc.Col(html.H4("Cifras Internacionales"),
               #         width={'size': 1,  "offset": 3}),
           ]),
    
#Cintillo 00    
    dbc.Row(
           [
               dbc.Col(html.H6(d2),           #Fecha de actualización
               width={'size' : "auto",
                      'offset' : 4}), 
           ]),  
    dbc.Row(
           [
               dbc.Col(html.H6("Fuente: SENSNSP"),
                        width={'size': 3,  "offset":1 }),
            ]),
       html.Hr(),
#cintillo 0
     dbc.Row(
           [
               dbc.Col(html.H5("2015")),
               dbc.Col(html.H5("2016")),
               dbc.Col(html.H5("2017")),
               dbc.Col(html.H5("2018")),
               dbc.Col(html.H5("2019")),
               dbc.Col(html.H5("2020")),
           ]),#justify= "start"),
    
#Cintillo 1
    dbc.Row(
           [
               dbc.Col(html.H2(conf_2015)),
               dbc.Col(html.H2(conf_2016)),
               dbc.Col(html.H2(conf_2017)),
               dbc.Col(html.H2(conf_2018)),
               dbc.Col(html.H2(conf_2019)),
               dbc.Col(html.H2(conf_2020)),
            ]),#justify= "start"),
    
# Cintillo 1.1
     dbc.Row(
           [
               dbc.Col(dcc.Graph(figure=mapa2015)),
               dbc.Col(dcc.Graph(figure=mapa2016)),
               dbc.Col(dcc.Graph(figure=mapa2017)),
               dbc.Col(dcc.Graph(figure=mapa2018)),
               dbc.Col(dcc.Graph(figure=mapa2019)),
               dbc.Col(dcc.Graph(figure=mapa2020)),
            ]),#justify= "start"),
    
    
       html.Hr(),
       html.Hr(),
       html.Hr(),
       html.Hr(),
       html.Hr(),
       html.Hr(),
       html.Hr(),
       html.Hr(),
       html.Hr(),
       html.Hr(),

# Cintillo 2
     dbc.Row(
           [
               dbc.Col(html.H3("Feminicidios por día")),
               dbc.Col(html.H3("Donde ocurrieron")),
               dbc.Col(html.H3("Rango de edad")),
               dbc.Col(html.H3("Tipo de victima")),
               dbc.Col(html.H3("Modus operandi")),
               dbc.Col(html.H3("Otras variables")),
            ], justify= "end"),
    
       html.Hr(),
       html.Hr(),
       html.Hr(),
       html.Hr(),
       html.Hr(),
       html.Hr(),
       html.Hr(),
#---------Grafica mensual
     dbc.Row([dbc.Col(dcc.Graph(figure=graf_meses, config= "autosize"))]),
    
    
# Cintillo 3
       
       html.Hr(),
            dbc.Row([
           
           dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/CamaraDiputados/blob/main/application/static/logocamara.jfif?raw=true"),
                        width=4, lg={'size': 1,  "offset": 3, }),
            
           dbc.Col(html.H6(" S e c r e t a r í a   G e n e r a l," 
                           " Secretaría de Servicios Parlamentarios, "
                           " México, 2021 "),
                  width={'size': 3, 'offset': 0}),
               ], justify="start",),
        
            ])


app.layout = html.Div([body])

from application.dash import app
from settings import config

if __name__ == "__main__":
    app.run_server()
