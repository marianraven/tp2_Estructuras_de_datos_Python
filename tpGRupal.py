####################################################################################################
#                       FUNCIONES AUXILIARES PARA IMPLEMENTACIÓN EN CÓDIGO PRINCIPAL
####################################################################################################
def calcularPromedio(men, may,con):
    resultado= ((men+may)/con)
    print(f'el promedio es {resultado}')   
    return resultado
####################################################################################################
def calcularPrimosIntermedios(valor1, valor2):
    cont = 0
    
    for i in range(valor1, valor2):
        if es_primo(i) == True:
            cont += 1               
    print ("")  
    print ("Hay", cont, "numeros primos entre el menor y el maximo valor ingresado anteriormente") 
#---------------------------------------------------------------------------------------------------
def es_primo(num):
    if num < 2:    
        return False
    for i in range(2, num): 
        if num % i == 0:    
            return False
    return True    
####################################################################################################
hexa_map = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

def pasar_A_Hexa(numero):
    result = ""
    if numero == 0:
        return '0'
    while numero != 0:
        result += str(hexa_map[(numero % 16)])
        numero = numero // 16
    return result[::-1]
#---------------------------------------------------------------------------------------------------
def mostrarHexadecimal(valor1, valor2):

    print ("Los numeros en base 16 entre el menor numero y mayor ingresado anteriormente son:")
    for i in range (valor1, valor2):
        print(pasar_A_Hexa(i))


####################################################################################################
def mostrarBinarios(valorMinimo, valorMaximo):
    print ("Los numeros en base 2 entre el menor y mayor ingresado anteriormente son: ")
    for i in range (valorMinimo, valorMaximo):
        print (binarizar(i))  

#---------------------------------------------------------------------------------------------------  
def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

####################################################################################################
#                               PROGRAMA PRINCIPAL
####################################################################################################
#VARIABLES UTILIZADAS:
contador=0
mayor=0
menor=999999999999999999999999999999999999999999999999999999999999
#BUCLE CONDICIONAL  
while True:
    try:
       enteros=int(input('ingrese un número o la palabra "fin" para finalizar: '))
       contador+=1
       if enteros > mayor:
          mayor = enteros
       print(f'El numero mayor es: {mayor}')
       
       if enteros < menor:
          menor = enteros
       print(f'El numero menor es: {menor}')
       calcularPromedio(menor,mayor,contador)
       print(contador)

       if enteros<=0:
          print('ingrese un numero entero positivo')
          contador-=1
       
#MANEJAMOS LA PALABRA CLAVE FIN COMO UNA EXCEPCION
    except ValueError:
        if enteros in ["FIN", "Fin", "fin"]:
          print(f'Usted ha ingresado la palabra clave fin para terminar el programa, la cantidad de numeros ingresados es: {contador}')
         
          pedirNumeroEntero()
        break
####################################################################################################
#UTILIZAMOS UNA FUNCIÓN PARA EL MENÚ, QUE A SU VEZ UTILIZA VARIAS FUNCIONES DECLARADAS AL PRINCIPIO DEL CÓDIGO
#---------------------------------------------------------------------------------------------------
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
        calcularPrimosIntermedios(menor,mayor)
    elif opcion == 2:
        print ("Mostrar todos los números enteros entre el máximo y el mínimo, en base 16 (hexadecimal)  ")
        mostrarHexadecimal(menor,mayor)
    elif opcion == 3:
        print("Mostrar todos los números enteros entre el máximo y el mínimo, en base 2 (binario)")
        mostrarBinarios(menor,mayor)
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin ")
####################################################################################################
#                                      TRABAJO FINALIZADO 
#################################################################################################### 

