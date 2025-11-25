#contruir un codigo de py que genere mil datos asociado a las ventas de un local de ropa 

#MOCK ejercicio que utilizamos para sumilar datos 
#def funcion en py
import random

from datetime import datetime,timedelta

def generar_ventas():

    productos=[
        {"nombre": "camiseta POLO", "precio" :150000},
        {"nombre": "pantalon clasico", "precio" :300000},
        {"nombre": "chaqueta cuerina", "precio" :450000},
        {"nombre": "camisa clasica", "precio" :200000},
        {"nombre": "camisa manga larga" ,"precio" :150000},
        {"nombre": "pantalon corto", "precio" :350000},
        {"nombre": "vestido largo ", "precio" :450000},
        {"nombre": "vestido corto", "precio" :280000},
        {"nombre": "vestido de jeans", "precio" :120000},
        {"nombre": "vestido de cuero", "precio" :120000}


    ]

    tallas=["S","M","L","XL"]
    vendedores=["Carla Morales","Salome Perez","Estefania soto","Zoe Muñoz","Sara gil",]

    tiendas=["Santafe","Florida","El Tesoro","San Diego","Unicentro", "Oviedo", "Arkadia", "La central"]

    fechaInicio=datetime(2025,1,1)

    #generar 1000  ventas
    ventas=[]
    for _ in range(1000):
        producto=random.choice(productos)
        cantidad=random.randint(1,8)
        fecha=fechaInicio + timedelta(days=random.randint(0,90))
        ventas.append(
            {
              "producto":producto["nombre"],
              "precioUnitario":producto["precio"],
              "cantidad":cantidad,
              "talla":random.choice(tallas),
              "tienda":random.choice(tiendas),
              "vendedor":random.choice(vendedores),
              "total":cantidad*producto["precio"]
            }
        )     
    return(ventas)         
