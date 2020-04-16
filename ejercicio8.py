#Escribir la función máximo, que recibe 2 numeros por parámetro y retorna el mayor.
#Luego, usando esta función, escriba un programa que pida 10 números al usuario por
#teclado y al finalizar informe el mayor por pantalla.
def maximus(n1,n2):
    if(n1<n2):
        mayor=n2
    else:
        mayor=n1
    print(mayor)
    return mayor  


for i in range(5):
    num1= int(input('ingrese el parametro 1: ')) 
    num2= int(input('ingrese el parametro 2: '))   
    maximus(num1,num2)
    guardar=maximus.mayor
