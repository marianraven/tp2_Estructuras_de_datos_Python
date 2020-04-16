#Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función
#debe recibir el importe sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la
#factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un
#21%.  0.21 , o sino t lo multiplica x 21
importeComun=float(input('Ingrese el monto de la factura sin iva: '))


def calcularTotalFacturaConIva(a, porcentajeDeIva=0.21):#si no pongo el valor 2 toma este por default
       
       v=1+porcentajeDeIva
       return (a*v)
print(calcularTotalFacturaConIva(100,0.1))#si le paso a la funcion un numero diferente al iva aplica el calculo con el nuevo valor
     