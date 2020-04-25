
 
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
    print ("4. Salir")
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print ("Mostrar todos los números enteros primos que se encuentran entre el máximo y el mínimo ingresado anteriormente.  ")
    elif opcion == 2:
        print ("Mostrar todos los números enteros entre el máximo y el mínimo, en base 16 (hexadecimal)  ")
    elif opcion == 3:
        print("Mostrar todos los números enteros entre el máximo y el mínimo, en base 2 (binario)")
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
     