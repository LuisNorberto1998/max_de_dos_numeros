# -*- coding: cp1252 -*-
"""
Definir una función max() que tome como argumento dos números
y devuelva el mayor de ellos o te indique si son iguales.

Es cierto que python tiene una función max() incorporada,
pero hacerla nosotros mismos es un muy buen ejercicio.

"""
x = 0 #Usaremos x como primer variable 
y = 0 #Usaremos y como segunda variable

def max(x,y): #Se define el nombre de la funcion y las variables que la integraran
    x = int(raw_input("Numero 1: ")) #Usamos la entrada de datos como entero
    y = int(raw_input("Numero 2: "))
    if x > y: #Se usa if para poner condicion a cada proceso
        print x, " es mayor que ", y
    elif y > x:
        print y, " es mayor que ", x
    elif x == y:
        print "Ambos numeros son iguales: ", x

max(x,y) #Llamamos nuestra funcion y se debera ejecutar correctamente
