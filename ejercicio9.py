#Escribir una función que dado un tiempo en horas, minutos y segundos retorne esa
#misma cantidad en segundos.
horas=int(input('ingrese las horas: '))
minutos=int(input('ingrese los minutos: '))
segundos=int(input('ingrese los segundos: '))

def convertir(a,b,c):
    y=(a/60)
    z=(y/60)
    x=(b/60)
    transformacion= z+x+c
    print(transformacion)
    return transformacion
    
convertir(horas, minutos, segundos)    