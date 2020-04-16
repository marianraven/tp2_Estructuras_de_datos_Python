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

empezar()

    