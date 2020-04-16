#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de
#un cilindro usando la primera función.
def calcular_Area(radioCirculo):
     areaCirculo=((radioCirculo * radioCirculo) * pi)
     return areaCirculo
    

def volumen_cilindro(resultado, altura):
    volumen=(pi*(resultado**2)*altura)
    return volumen

pi= 3.14
radioCirculo=int(input("Ingrese el radio del circulo:"))
area=calcular_Area(radioCirculo)
print("El area del circulo es:  ",area)
alturaCilindro= int(input("ingrese la altura del cilindro: "))
calculo= volumen_cilindro(area, alturaCilindro)
print('El volumen del cilindro es: ', calculo)



