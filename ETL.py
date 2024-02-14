#HUMEDAD, TEMPERATURA,DIRECCION DEL VIENTO,VELOCIDAD DEL VIENTO
import pandas as pd
import os
import glob 
import numpy as np
all_files=glob.glob(r"C:\Users\herca\OneDrive\Documentos\Python Scripts\datos direccion cdmx\Meteorologia\*.csv")
file_list=[]
for f in all_files:
    data=pd.read_csv(f)
    nombre=os.path.basename(f)
    data['source_file']=nombre  # en este for leemos todos los archivos que obtuvimos en este directorio
    file_list.append(data)
    
df=pd.concat(file_list, ignore_index=True) #Mostramos el Dataframe concatenado
df.drop(['unit', 'source_file'], axis=1, inplace=True)# #### quitando columnas que no sirven
df.dropna(inplace=True)#### quitando las filas que no sirven (contienen valores nulos)
df.drop(df[(df['id_station'] !='TLA') ].index, inplace=True) ##conservando solo los datos de las estaciones que nos interesan
numelist=list(range(41, 50))
my_dict = "41|42|43|44|45|46|47|48|49"
df=df [df ["date"]. str .contains (my_dict) == False ] ##Qitando los datos que no son fechas
df_rh=df[df["id_parameter"].str.contains("RH")] #Datframe de humedad
df_rh.rename(columns={'id_parameter':'Parametro_Humedad','value':'Humedad'}, inplace=True)
df_rh.drop(['id_station'], axis=1, inplace=True)# #### quitando columnas que no sirven
df_tmp=df[df["id_parameter"].str.contains("TMP")] #Datframe de temnperatura
df_tmp.rename(columns={'id_parameter':'Parametro_tmp','value':'Temperatura'}, inplace=True)
df_tmp.drop(['id_station'], axis=1, inplace=True)# #### quitando columnas que no sirven
df_wdr=df[df["id_parameter"].str.contains("WDR")] #Dataframe de direccion de viento
df_wdr.rename(columns={'id_parameter':'Parametro_Dir','value':'Direccion_Viento'}, inplace=True)
df_wsp=df[df["id_parameter"].str.contains("WSP")] #Dataframe de velocidad del viento
df_wsp.rename(columns={'id_parameter':'Parametro_Velocidad','value':'Velocidad_Viento'}, inplace=True)
df_wsp.drop(['id_station'], axis=1, inplace=True)# #### quitando columnas que no sirven
df_rh.drop(['Parametro_Humedad'], axis=1, inplace=True)# #### quitando columnas que no sirven
df_tmp.drop(['Parametro_tmp'], axis=1, inplace=True)# #### quitando columnas que no sirven
df_wdr.drop(['Parametro_Dir'], axis=1, inplace=True)# #### quitando columnas que no sirven
df_wsp.drop(['Parametro_Velocidad'], axis=1, inplace=True)# #### quitando columnas que no sirven
union=pd.merge(df_wdr, df_wsp,on="date", how="outer").merge(df_tmp, on="date",how="outer").merge(df_rh,on="date",how="outer")
union.drop(['id_station'], axis=1, inplace=True)
union.rename(columns={'date':'Fecha_Hora'}, inplace=True)
union.to_excel('Met_limpio_cdmx.xlsx', index=False) ##Escribir el dataframe resultante en un excel
##################################################################################################
#LLUVIA ACUMULADA
all_files = glob.glob(r"C:\Users\herca\OneDrive\Documentos\Python Scripts\datos observatorio\acumulada por año\*.csv")
file_list = []
for f in all_files:
    data = pd.read_csv(f)
    nombre = os.path.basename(f)
    data['source_file'] = nombre  # en este for leemos todos los archivos que obtuvimos en este directorio
    file_list.append(data)
    
df = pd.concat(file_list, ignore_index=True) #Mostramos el Dataframe concatenado
df.dropna(inplace=True)  # quitando las filas que no sirven (contienen valores nulos)
df.drop(['source_file'], axis=1, inplace=True)  # quitando columnas que no sirven
df['Fecha/hora'] = pd.to_datetime(df['Fecha/hora']).dt.strftime('%d/%m/%Y %H:%M')# Convertir el formato de la columna 'Fecha/hora'
df_filtered_acum = df[df['Fecha/hora'].str[-2:] == '00']# Filtrar los registros que tienen la hora exacta sin minutos
df_filtered_acum.to_excel('Lluvia_Acumulada_limpio_cdmx.xlsx', index=False)# Escribir el DataFrame resultante en un archivo de Excel
##################################################################################################
#LLUVIA INTENSIDAD
all_files = glob.glob(r"C:\Users\herca\OneDrive\Documentos\Python Scripts\datos observatorio\intensidad por año\*.csv")
file_list = []
for f in all_files:
    data = pd.read_csv(f)
    nombre = os.path.basename(f)
    data['source_file'] = nombre  # en este for leemos todos los archivos que obtuvimos en este directorio
    file_list.append(data)
    
df = pd.concat(file_list, ignore_index=True) #Mostramos el Dataframe concatenado
df.dropna(inplace=True)  # quitando las filas que no sirven (contienen valores nulos)
df.drop(['source_file'], axis=1, inplace=True)  # quitando columnas que no sirven
df.drop(['Estación'], axis=1, inplace=True)
df['Fecha/hora'] = pd.to_datetime(df['Fecha/hora']).dt.strftime('%d/%m/%Y %H:%M')# Convertir el formato de la columna 'Fecha/hora'
df_filtered_inten= df[df['Fecha/hora'].str[-2:] == '00']# Filtrar los registros que tienen la hora exacta sin minutos
df_filtered_inten.to_excel('Lluvia_intesidad_limpio_cdmx.xlsx', index=False)# Escribir el DataFrame resultante en un archivo de Excel
union_lluvia=pd.merge(df_filtered_acum,df_filtered_inten, on="Fecha/hora", how="outer")
union_lluvia.drop(['Estación'], axis=1, inplace=True)
union_lluvia.rename(columns={'Fecha/hora':'Fecha_Hora','Acumulada [mm]':'Lluvia_Diaria','Intensidad [mm/h]':'Lluvia_Actual'}, inplace=True)
union_lluvia.to_excel('lluvia_union.xlsx',index=False)
##################################################################################################
#PRESION
all_files=glob.glob(r"C:\Users\herca\OneDrive\Documentos\Python Scripts\datos direccion cdmx\MeteologiaPresion\*.csv")
file_list=[]
for f in all_files:
    data=pd.read_csv(f)
    nombre=os.path.basename(f)
    data['source_file']=nombre  # en este for leemos todos los archivos que obtuvimos en este directorio
    file_list.append(data)
    
df=pd.concat(file_list, ignore_index=True) #Mostramos el Dataframe concatenado
df.drop(['unit', 'source_file', 'parameter'], axis=1, inplace=True)# #### quitando columnas que no sirven
df.dropna(inplace=True)#### quitando las filas que no sirven (contienen valores nulos)
df.drop(df[(df['cve_station'] !='TLA') ].index, inplace=True) ##conservando solo los datos de las estaciones que nos interesan
my_dict = "41|42|43|44|45|46|47|48|49"
df=df [df ["Date"]. str .contains (my_dict) == False ] ##Qitando los datos que no son fechas
df.drop(['cve_station'], axis=1, inplace=True)
df.rename(columns={'Date':'Fecha_Hora','value':'Presion_Atmosferica'}, inplace=True)
df.to_excel('presion_limpio.xlsx', index=False) ##Escribir el dataframe resultante en un excel
#####################################################################################################
#DATOS TABLA "variables_meteorologicas"
variables_totales = pd.merge(union, union_lluvia, on="Fecha_Hora", how="outer").merge(df, on="Fecha_Hora", how="outer")
variables_totales["Id_Resgistro_Datos"] = range(1, len(variables_totales) + 1)
variables_totales["Id_Estacion"] = ""
variables_totales = variables_totales[["Id_Resgistro_Datos", "Id_Estacion", "Fecha_Hora", "Temperatura", "Velocidad_Viento", "Direccion_Viento", "Lluvia_Actual", "Lluvia_Diaria", "Presion_Atmosferica", "Humedad"]]
variables_totales = variables_totales.replace(np.nan, 0)

# Convierte la columna de fechas a objetos datetime
variables_totales['Fecha_Hora'] = pd.to_datetime(variables_totales['Fecha_Hora'], format='%d/%m/%Y %H:%M')

# Ordena el DataFrame por la columna de fechas
variables_totales = variables_totales.sort_values(by='Fecha_Hora')

# Guarda el DataFrame ordenado en un nuevo archivo Excel
variables_totales.to_excel('variables_meteorologicas_ordenado.xlsx', index=False)
#####################################################################################################
#DATOS TABLA "cdmx_historico"
cdmx_historico=variables_totales
cdmx_historico["Id_CDMX"] = range(1, len(variables_totales) + 1)
cdmx_historico = variables_totales[["Id_CDMX","Id_Estacion", "Fecha_Hora", "Temperatura", "Velocidad_Viento", "Direccion_Viento","Presion_Atmosferica","Humedad"]]
cdmx_historico.to_excel('cdmx_historico.xlsx',index=False)
#####################################################################################################
#DATOS TABLA "cdmx_unam"
cdmx_unam=variables_totales
cdmx_unam["Id_UNAM"] = range(1, len(variables_totales) + 1)
cdmx_unam = variables_totales[["Id_UNAM","Id_Estacion", "Fecha_Hora", "Lluvia_Actual","Lluvia_Diaria"]]
cdmx_unam.to_excel('cdmx_unam.xlsx', index=False)


