#Escribir una función que recibe dos números enteros mayores que 1, n y m, y retorna
#la potencia n m
num1=int(input('Escribir número uno: '))
num2= int(input('Escribir número dos: '))

def funcion_potencia(n, m):
    if n<1 or m <1  :
       print('Error con los numeros ingresados, deben ser mayores que 1')
    else:
       contador = 1  # Simple ayudante del ciclo
       elevado = 1  # Aquí almacenamos el resultado de ir multiplicando el número
    # Hacer un ciclo desde 1 hasta el exponente, para multiplicarlo ese número de veces
       while contador <= m:
          elevado = elevado * n
          contador = contador + 1
    print(elevado)
    return elevado
    

funcion_potencia(num1,num2)
