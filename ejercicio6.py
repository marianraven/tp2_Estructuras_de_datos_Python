#Escribir una función que recibe tres numeros enteros por parámetros, calcula el
#promedio y retorna “APROBADO” si el promedio es mayor o igual a 7 o
#“DESAPROBADO” si es menor.

entero1= int(input('ingrese parametro 1: '))
entero2= int(input('ingrese parametro 2: '))
entero3= int(input('ingrese parametro 3: '))

def calcularPromedio(uno,dos,tres):

    resultado= ((uno+dos+tres)/3)
    
    if resultado<7.0:
        print('reprobado')
    elif resultado==7.0 or resultado <10.0:
        print('Aprobado')   
    else :
        print('alguno de los digitos ingresados es incorrecto')    
    return resultado

calcularPromedio(entero1,entero2,entero3)         