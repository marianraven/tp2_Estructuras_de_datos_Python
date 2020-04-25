#Escribir un procedimiento que muestre por pantalla la cadena “Hola mundo!!!” cada
#vez que se la invoque

cadena='Hola Mundo!!!'

def empezar():
  entrada= int(input('Ingrese 1 para invocar funcion, o 0 para salir'))
  if entrada==1:
        invocar(cadena)
  if entrada==0:
        print('Usted ha finalizado las funciones')
    
  else:
        print('Usted ha ingresado un numero no valido')
        empezar()



def invocar(miCadena):
    print(miCadena)
    empezar()
####################################################################################################
#Escribir un procedimiento que se le pase por parámetros una cadena <nombre> y
#muestre por pantalla: “Hola <nombre>!!!”


def pasoParametro(n):
      print(f'Hola {n}')
    
####################################################################################################

#Escribir una función que calcule y retorne el factorial de un numero natural. 
# La operación factorial (!) se define de la siguiente manera:
#N !={1
#si N = 0 = N ( N − 1)( N −2) ...3.2.1
#N ( N −1) ! si N >0
#}

def factorial(n): 
    resultado = 1
    i = 1
    while i <= n:
        resultado = resultado * i
        i = i + 1
    return print(resultado)
      
####################################################################################################
#Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función
#debe recibir el importe sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la
#factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un
#21%.  0.21 , o sino t lo multiplica x 21

def calcularTotalFacturaConIva(a, porcentajeDeIva=0.21):#si no pongo el valor 2 toma este por default
       
       v=1+porcentajeDeIva
       return (a*v)

#si le paso a la funcion un numero diferente al iva aplica el calculo con el nuevo valor
     
####################################################################################################
# #Escribir una función que calcule el área de un círculo y otra que calcule el volumen de
#un cilindro usando la primera función.
def calcular_Area(radioCirculo):
     areaCirculo=((radioCirculo * radioCirculo) * pi)
     return areaCirculo
    

def volumen_cilindro(resultado, altura):
    volumen=(pi*(resultado**2)*altura)
    return volumen


####################################################################################################
# #Escribir una función que recibe tres numeros enteros por parámetros, calcula el
#promedio y retorna “APROBADO” si el promedio es mayor o igual a 7 o
#“DESAPROBADO” si es menor.
def calcularPromedio(uno,dos,tres):

    resultado= ((uno+dos+tres)/3)
    
    if resultado<7.0:
        print('reprobado')
    elif resultado==7.0 or resultado <10.0:
        print('Aprobado')   
    else :
        print('alguno de los digitos ingresados es incorrecto')    
    return resultado


####################################################################################################

#Escribir una función que recibe dos números enteros mayores que 1, n y m, y retorna
#la potencia n m


def funcion_potencia(n, m):
    if n<1 or m <1  :
       print('Error con los numeros ingresados, deben ser mayores que 1')
    else:
       contador = 1  # Simple ayudante del ciclo
       elevado = 1 
       while contador <= m:
          elevado = elevado * n
          contador = contador + 1
    print(elevado)
    return elevado
    


####################################################################################################

#Escribir la función máximo, que recibe 2 numeros por parámetro y retorna el mayor.
#Luego, usando esta función, escriba un programa que pida 10 números al usuario por
#teclado y al finalizar informe el mayor por pantalla.


####################################################################################################

#Escribir una función que dado un tiempo en horas, minutos y segundos retorne esa
#misma cantidad en segundos.

def convertir(a,b,c):
    y=(a/60)
    z=(y/60)
    x=(b/60)
    transformacion= z+x+c
    print(transformacion)
    
####################################################################################################
#Escribir una función que dado un año, retorne verdadero si es bisiesto y falso en caso
#contrario.
#Nota: Los años bisiestos son múltiplos de 4 o de 400, pero los múltiplos de 100 no lo
#son. Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no
#es bisiesto, 2000 es bisiesto, 1900 no es bisiesto

def anio_bisiesto(anio):
  
  if anio % 4 == 0:
      if anio % 100 == 0:
          if anio % 400 == 0:
              print(f'El año : {anio},es bisiesto')
          else:
              print(f'El año: {anio},no es bisiesto')
      else:
          print(f'El año: {anio}, es bisiesto.')
  else:
      print(f'El año: {anio}, no es bisiesto.')

####################################################################################################
#Escribir un programa que pida dos años al usuario y escriba cuántos años bisiestos
#hay entre esas dos fechas (incluidos los dos años).
def cuantos_bisiestos_hay(anio1,anio2):
    contador=0

    for anio1 in range(anio2):
        anio= anio1+1
        if anio % 4 == 0:
           if anio % 100 == 0:
              if anio % 400 == 0:
                  contador+=1
                  print(f'El año : {anio},es bisiesto')
              else:
                 print('')
           else:
                contador+=1
                print(f'El año: {anio}, es bisiesto.')
        else:
            print('')

    print(f'desde el año: {anio1}, hasta el año : {anio2} hay {contador} años bisiestos')



####################################################################################################
#Escribir una función que tome por parámetro un numero entero y retorne la suma de
#sus dígitos.
#Escribir una función que tome por parámetro un numero entero y retorne la suma de
#sus dígitos.

 
def suma_dig(n):
   suma=0
   if (n < 0):
        n=-n
   while (n!=0) :
      suma+=n%10          #  /* Sumamos la última cifra, que se obtiene
                                #   calculando el resto módulo 10 del número.
                                #   Por ejemplo, la última cifra de 12345 es
                                #   12345 % 10 = 5. */
      n=n/10             #  /* Repetimos el proceso para el número sin
                                #   la última cifra, que se obtiene calculando
                                #   el cociente de dividir el número original
                                #   por 10. Por ejemplo, 12345/10 =1234. */
   print(f"La suma de los digitos del numero arriba{suma}") 

####################################################################################################
#Escribir un programa que pida números positivos al usuario. Mostrar el número cuya
#sumatoria de dígitos fue mayor y la cantidad de números cuya sumatoria de dígitos
#fue menor que 10. Utilizar una o más funciones, según sea necesario.




####################################################################################################
#Escribir un programa que solicita al usuario el ingreso de números primos. La lectura
#finalizará cuando ingrese un número que no sea primo. Por cada número, mostrar la
#suma de sus dígitos. Al finalizar el programa, mostrar el factorial del mayor número
#ingresado. Utilizar una o más funciones, según sea necesario


####################################################################################################



def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
  
    print ("1. Opcion 1")
    print ("2. Opcion 2")
    print ("3. Opcion 3")
    print ("4. Opcion 4")
    print ("5. Opcion 5")
    print ("6. Opcion 6")
    print ("7. Opcion 7")
    print ("8. Opcion 8")
    print ("9. Opcion 9")
    print ("10. Opcion 10")
    print ("11. Opcion 11")
    print ("12. Salir")
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print("invocar funcion hola mundo")
        empezar()
      
    elif opcion == 2:
        
        print("funcion con parametros ingrese su nombre") 
        nom=str(input("ingrese su nombre:"))
        pasoParametro(nom)

    elif opcion == 3:
        numeroIngresado=int(input('Ingrese un número y recibirá el calculo de su factorial: '))
        factorial(numeroIngresado)    

    elif opcion == 4:
        print("calcular iva")
        importeComun=float(input('Ingrese el monto de la factura sin iva: '))
        print(calcularTotalFacturaConIva(importeComun))
        
    elif opcion == 5:
        print("calcular area de un circulo y volumen de un cilindro")       
        pi= 3.14
        radioCirculo=int(input("Ingrese el radio del circulo:"))
        area=calcular_Area(radioCirculo)
        print("El area del circulo es:  ",area)
        alturaCilindro= int(input("ingrese la altura del cilindro: "))
        calculo= volumen_cilindro(area, alturaCilindro)
        print('El volumen del cilindro es: ', calculo)
       
    elif opcion == 6:
        print("funcion para promedios")

        entero1= int(input('ingrese parametro 1: '))
        entero2= int(input('ingrese parametro 2: '))
        entero3= int(input('ingrese parametro 3: '))

        calcularPromedio(entero1,entero2,entero3)  

    elif opcion == 7:
        print("potencia de un numero:")
        num1=int(input('Escribir número uno: '))
        num2= int(input('Escribir número dos: '))
        funcion_potencia(num1,num2)

    elif opcion == 8:
        print("conversor a minutos")
        horas=int(input('ingrese las horas: '))
        minutos=int(input('ingrese los minutos: '))
        segundos=int(input('ingrese los segundos: '))

        convertir(horas, minutos, segundos)    

    elif opcion == 9:
        print("funcion año bisiesto")
        ingreso = int(input('Ingresa un año: '))
        anio_bisiesto(ingreso)

    elif opcion == 10: 
        print("calcular años bisiestos entre:")
        entrada1=int(input('ingrese el primer año: '))
        entrada2= int(input('ingrese el segundo año: '))
        cuantos_bisiestos_hay(entrada1,entrada2)

    elif opcion == 11:
        print("sumar digitos")
        numero=int(input("Por favor, introduzca un numero entero positivo: ")) 
        suma_dig(numero)
        
    elif opcion == 12:
         salir==True
        
        
    else:
        print ("Introduce un numero válido")
 
print ("Fin ")
pedirNumeroEntero()