#Escribir una función que calcule y retorne el factorial de un numero natural. 
# La operación factorial (!) se define de la siguiente manera:
#N !={1
#si N = 0 = N ( N − 1)( N −2) ...3.2.1
#N ( N −1) ! si N >0
#}
numeroIngresado=int(input('Ingrese un número y recibirá el calculo de su factorial: '))

def factorial(n): 
    resultado = 1
    i = 1
    while i <= n:
        resultado = resultado * i
        i = i + 1
    return print(resultado)
    

factorial(numeroIngresado)    