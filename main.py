#COMO USAR PANDAS PARA CREAR FILTROS 

#1 IMPORTARLO
import pandas as pd

#2 TRAER LOS DATOS
from data.simulador import generar_ventas

#3  CONVERTIR LOS DATOS  EN UN DATAFRAME
dataFrame=pd.DataFrame(generar_ventas())
#4 APLICAR LOS FILTROS (5)
#print(dataFrame)

#Yo como administrador de la tienda quiero  obtener  las ventas de salome perez
filtrouno=dataFrame.query("vendedor=='Salome Perez'")
#print(filtrouno)

#Yo como administrador de la tienda quiero ver ventas con mas de tres productos
filtrodos=dataFrame.query("cantidad >=3")
#print(filtrodos)

#Yo como administrador de la tienda quiero ver ventas con valores de mas de 900 mil pesos 
filtrotres=dataFrame.query("total > 900000")
#print(filtrotres)


#Yo como administrador de la tienda quiero ver ventas de las  vestidos 
filtrocuatro=dataFrame.query("producto == 'vestidos' ")
#print(filtrocuatro)


#Yo como administrador de la tienda quiero ver ventas  de los productos que menos se venden 
filtrocinco=dataFrame.query("cantidad <=1")
print(filtrocinco)