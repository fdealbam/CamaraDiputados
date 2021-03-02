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


yesterday = datetime.now() - timedelta(1)
yea = datetime.strftime(yesterday, '%Y%m%d')

today = date.today()
d2 = today.strftime("Fecha de actualización : %d de %B de %Y")






###############################
# DATABASES
############################### Abre archivos

base = pd.read_csv('https://raw.githubusercontent.com/winik-pg/exercises_pythoncitos/master/mun_p1_cvegeo.csv', encoding='latin-1', usecols=['Nom_Ent','nom_mun','cve_ent_mun1','cve_ent_mun2'])
contagios = pd.read_csv("https://datos.covid-19.conacyt.mx/Downloads/Files/Casos_Diarios_Municipio_Confirmados_%s.csv" %(yea))
decesos = pd.read_csv("https://datos.covid-19.conacyt.mx/Downloads/Files/Casos_Diarios_Municipio_Defunciones_%s.csv" %(yea))
SS = ('https://datos.covid-19.conacyt.mx/')
autores = ('https://raw.githubusercontent.com/winik-pg/exercises_pythoncitos/master/Autores.docx')





# TRATAMIENTO 
###############################   Contagios  por día

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
# by moths 

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
#cont_mar21 = contagios2[(contagios2.days.dt.year == 2021 ) & (contagios2.days.dt.month == 3)]


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
#contagios_mar21 = cont_mar21.cases.sum()



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
#contagios_mar21_prom = round(cont_mar21.cases.mean())



###############################   Contagios por dia  

endall1 = len(decesos)
decesos1 = decesos.iloc[:,3:endall1].sum().T
decesos2 = pd.DataFrame(decesos1)
decesos2['index'] = decesos2.index 
decesos2.rename(columns = {0:'cases', 'index':'days'}, inplace = True)


############################### Total de decesos 
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
#dec_mar21 = decesos2[(decesos2.days.dt.year == 2021 ) & (decesos2.days.dt.month == 3)]



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
#decesos_mar21 = dec_mar21.cases.sum()


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
#decesos_mar21_prom = round(dec_mar21.cases.mean())



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

############################################# Grafica1
figaro = go.Figure()
figaro.add_trace(go.Bar(x=contagios2['days'],y=contagios2['cases'],
                #name='Contagios confirmados COVID-19',
                marker_color='firebrick'  # cambiar nuemeritos de rgb
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
        tickfont_size=12,
        titlefont_family= "Monserrat"),
    #autosize=False,
    #width=1000,
    #height=400
    )

############################################ Grafica 2

figaro2 = go.Figure()
figaro2.add_trace(go.Bar(x=decesos2['days'],y=decesos2['cases'],
                #name='Contagios confirmados COVID-19',
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

############################### 1 Titulo Contagios totales 
patabla2 = {'Contagios': [str(f"{contagiostotal:,d}")] }    
patabla3 = pd.DataFrame (patabla2)

############################### 2 Titulo Decesos totales 
patabla2a = {'Decesos': [str(f"{decesos_tot:,d}") ] }
patabla3a = pd.DataFrame (patabla2a)

###################################################Tabla meses
patabla6 = {
            'febrero20'   : [str(f"{contagios_feb20:,d}")],#, decesos_feb20],
            'marzo20'     : [str(f"{contagios_mar20:,d}")],#, decesos_mar20],
            'abril20'     : [str(f"{contagios_abr20:,d}")],#, decesos_abr20],
            'mayo20'      : [str(f"{contagios_may20:,d}")],#, decesos_may20],
            'junio20'     : [str(f"{contagios_jun20:,d}")],#, decesos_jun20],
            'julio20'     : [str(f"{contagios_jul20:,d}")],#, decesos_jul20],
            'agosto20'    : [str(f"{contagios_ago20:,d}")],#, decesos_ago20],
            'septiembre20': [str(f"{contagios_sep20:,d}")],#, decesos_sep20],
            'octubre20'   : [str(f"{contagios_oct20:,d}")],#, decesos_oct20],
            'noviembre20' : [str(f"{contagios_nov20:,d}")],#, decesos_nov20],
            'diciembre20' : [str(f"{contagios_dic20:,d}")],#, decesos_dic20],
            'enero21'     : [str(f"{contagios_ene21:,d}")],#, decesos_ene21],
            'febrero21'   : [str(f"{contagios_feb21:,d}")],#, decesos_feb21],
                            }


patabla7 = pd.DataFrame (patabla6, columns = [#'blanc',
                                              'febrero20','marzo20','abril20','mayo20','junio20',
    'julio20','agosto20','septiembre20','octubre20','noviembre20','diciembre20',
                                              'enero21','febrero21'])

################################################################Cintillo mensual decesos
patabla6a = {
            'febrero20'   : [str(f"{decesos_feb20:,d}")],#, decesos_feb20],
            'marzo20'     : [str(f"{decesos_mar20:,d}")],#, decesos_mar20],
            'abril20'     : [str(f"{decesos_abr20:,d}")],#, decesos_abr20],
            'mayo20'      : [str(f"{decesos_may20:,d}")],#, decesos_may20],
            'junio20'     : [str(f"{decesos_jun20:,d}")],#, decesos_jun20],
            'julio20'     : [str(f"{decesos_jul20:,d}")],#, decesos_jul20],
            'agosto20'    : [str(f"{decesos_ago20:,d}")],#, decesos_ago20],
            'septiembre20': [str(f"{decesos_sep20:,d}")],#, decesos_sep20],
            'octubre20'   : [str(f"{decesos_oct20:,d}")],#, decesos_oct20],
            'noviembre20' : [str(f"{decesos_nov20:,d}")],#, decesos_nov20],
            'diciembre20' : [str(f"{decesos_dic20:,d}")],#, decesos_dic20],
            'enero21'     : [str(f"{decesos_ene21:,d}")],#, decesos_ene21],
            'febrero21'   : [str(f"{decesos_feb21:,d}")],#, decesos_feb21],
                            }

patabla7a = pd.DataFrame (patabla6a, columns = [
                                              'febrero20','marzo20','abril20','mayo20','junio20','julio20',
                                              'agosto20','septiembre20','octubre20','noviembre20','diciembre20',
                                              'enero21','febrero21'])

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
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='Contagios',
    title_font_family= 'Monserrat ExtraBold',
    title_font_color= 'white',
    title_font_size= 22,
    xaxis_tickfont_size= 3,
    yaxis=dict(
        titlefont_size=80,
        tickfont_size= 10,
        titlefont_family= 'Monserrat ExtraBold',
        ))

########################################################  2 Tasa Contagios
g10edosct = go.Figure()
g10edosct.add_trace(go.Bar(x=contaedos2a['tasa'],y=contaedos2a['Nom_Ent'],
                          orientation='h',
                #name='Contagios confirmados COVID-19',
                          marker_color='palevioletred',
                         ))
g10edosct.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='Tasa Contagios',
    title_font_family= 'Monserrat ExtraBold',
    title_font_color= 'white',
    title_font_size= 22,
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
                marker_color='olive',
                orientation='h'          
                # cambiar nuemeritos de rgb
                ))

g10edosd.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='Decesos',
    title_font_family= 'Monserrat ExtraBold',
    title_font_color= 'white',
    title_font_size= 22,
    xaxis_tickfont_size= 3,
    yaxis=dict(
        titlefont_size=80,
        tickfont_size= 10,
        titlefont_family= 'Monserrat ExtraBold',
        ))
############################################################ 4 Tasa de Letalidad
g10edosdt = go.Figure()
g10edosdt.add_trace(go.Bar(x=deceedos2a['tasa'],y=contaedos2a['Nom_Ent'],
                #name='Contagios confirmados COVID-19',
                marker_color='slategray',
                orientation='h'          
                # cambiar nuemeritos de rgb
                ))
g10edosdt.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='Tasa de Decesos',
    title_font_family= 'Monserrat ExtraBold',
    title_font_color= 'white',
    title_font_size= 22,
    xaxis_tickfont_size= 3,
    yaxis=dict(
        titlefont_size=80,
        tickfont_size= 10,
        titlefont_family= 'Monserrat ExtraBold',
         #autosize=True,
   
   
        ))

############################### Gráfica Pie de Contagios por estado

piec = px.pie(contaedog, values='total', names='Nom_Ent',
             color_discrete_sequence=px.colors.sequential.Reds,
             #title='Distribución de contagios',
             )
piec.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  uniformtext_minsize=10,
                  uniformtext_mode='hide',
                  #font_family= "Monserrat",
                  autosize=True,
                  width= 550,
                  height=550,
                  title_font_size = 12,
                  font_color="black",
                  title_font_color="firebrick",
                  #title_font_family = 'Monserrat ExtraBold' 
                   )


############################### Gráfica Pie de Deceso por estado

pied = px.pie(deceedosg, values='total', names='Nom_Ent',
             color_discrete_sequence=px.colors.sequential.Greys,
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
                  font_color="black",
                  title_font_color="black",
                  #title_font_family = 'Monserrat ExtraBold' 
                   )
# A P P

####################################

########### Define your variables
mytitle=' '
tabtitle='COVID-19 en México'
#githublink='https://github.com/Aeelen-Miranda/exercises_pythoncitos/blob/master/app.py'
sourceurl='https://datos.covid-19.conacyt.mx/'




app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
body = html.Div([
       html.H1("COVID-19 en México"),
       html.H3("Secretaría de Servicios Parlamentarios, Cámara de Diputados"),
       
       
       html.H4((d2)),
       html.Hr(),
       dbc.Table.from_dataframe(patabla3), #striped=True, bordered=False, hover=True,
       #                        style={'left': '3vw', 'top': '-75vh', 'width': '240px'})
       dbc.Row([dbc.Col(html.Div(dcc.Graph(figure=figaro, config= "autosize")))]),
       dbc.Table.from_dataframe(patabla7, size= "xsm"),
       #striped=True, bordered=True, hover=True)
       html.Hr(), #Espacio
       dbc.Table.from_dataframe(patabla3a), 
       dbc.Row([dbc.Col(html.Div(dcc.Graph(figure=figaro2, config= "autosize")))]),
       dbc.Table.from_dataframe(patabla7a, size= "xsm"),
       html.Hr(),
       html.H1('Las 10 entidades con más... '),
       dbc.Row([dbc.Col(html.Div(dcc.Graph(figure=g10edosc, config= "autosize")))]), #Contagios
       dbc.Row([dbc.Col(html.Div(dcc.Graph(figure=g10edosct,config= "autosize")))]), #TasaCont.
       dbc.Row([dbc.Col(html.Div(dcc.Graph(figure=g10edosd, config= "autosize")))]), #Decesos
       dbc.Row([dbc.Col(html.Div(dcc.Graph(figure=g10edosdt,config= "autosize")))]), #TasaLetalidad
       html.Hr(),
       html.H1('Alrededor de 60% de casos se concentran en... '),
       html.H3("Contagios"),
       dbc.Row([dbc.Col(html.Div(dcc.Graph(figure=piec,config= "autosize")))]),
       html.H3("Decesos"),
       dbc.Row([dbc.Col(html.Div(dcc.Graph(figure=pied,config= "autosize")))]),
])

app.layout = html.Div([body])

from application.dash import app
from settings import config
app.run_server(debug=config.debug, host=config.host, port=config.port)
