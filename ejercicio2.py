#Escribir un procedimiento que se le pase por parámetros una cadena <nombre> y
#muestre por pantalla: “Hola <nombre>!!!”
nombre= str(input('Ingrese su nombre: '))

def pasoParametro(n):
      print(f'Hola {n}')

pasoParametro(nombre)      