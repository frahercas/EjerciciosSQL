import pandas as pd
import os
import glob 
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy import create_engine,text
import sqlalchemy
#ESTABLECIENDO CONEXION CON BASE DE DATOS
cadena_conexion='mysql+mysqldb://admin:Passw0rd@pt.cllungh2p0o2.us-east-1.rds.amazonaws.com:3306/proyecto_final'
conexion=create_engine(cadena_conexion)



#################################################################################################################

#####################################################################################################
#ESCRIBIENDO LOS DATOS EN SUS RESPECTIVAS TABLAS
# df = pd.read_excel("zonas_estaciones.xlsx")
# df.to_sql(name='zonas_estaciones', con=conexion, schema="proyecto_final", index=False, if_exists='append')
# df1 = pd.read_excel("direccion_estaciones.xlsx")
# df1.to_sql(name='direccion_estaciones', con=conexion, schema="proyecto_final", index=False, if_exists='append')
# df2 = pd.read_excel("estaciones_meteorologicas.xlsx")
# df2.to_sql(name='estaciones_meteorologicas', con=conexion, schema="proyecto_final", index=False, if_exists='append')
# variables_totales = pd.read_excel("variables_meteorologicas_ordenado.xlsx")
# variables_totales.to_sql(name='variables_meteorologicas', con=conexion, schema="proyecto_final", index=False, if_exists='append')
cdmx_historico= pd.read_excel("cdmx_historico.xlsx")
cdmx_historico.to_sql(name='cdmx_historico', con=conexion, schema="proyecto_final", index=False, if_exists='append')
cdmx_unam= pd.read_excel("cdmx_unam.xlsx")
cdmx_unam.to_sql(name='cdmx_unam', con=conexion, schema="proyecto_final",index=False,if_exists='append')

# pred24=pd.read_excel("pred24.xlsx")
# pred24.to_sql(name='predicciones_24hr', con=conexion, schema="proyecto_final", index=False,if_exists='append')
# pred31=pd.read_excel("pred31.xlsx")
# pred31.to_sql(name='predicciones_31d', con=conexion, schema="proyecto_final",index=False,if_exists='append')