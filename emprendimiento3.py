# Considera ahora una tercera versión llamada emprendedor3.py utilizando la fórmula
# original de utilidades donde el usuario ingrese el precio de suscripción P, el número de
# usuarios normales U y los gastos GT. Adicionalmente, solicita las utilidades del año
# anterior Uanterior, todo esto mediante input(). El programa debe calcular las utilidades
# actuales y mostrar la razón entre las utilidades actuales y las del año anterior con dos
# decimales.
# (2 Puntos)

# CREACION DE VARIABLES
 
precioSuscripcion = 0

numeroUsuarios = 0 

gastoTotal = 0

utilidadesPasado = 0

utilidadesActuales = 0

utilidadesTotales = float

# SOLICITANDO DATOS AL USUARIO

numeroUsuarios =int(input("Ingrese la cantidad de usuarios: \n")) 

precioSuscripcion = float(input("Ingrese el precio de la suscripción: \n"))

gastoTotal = float(input("Ingrese el gasto operacional: \n"))

utilidadesPasado = float(input("Ingrese las utilidades del año pasado: \n"))

# SOLUCION DEL PROBLEMA

utilidadesActuales = (precioSuscripcion * numeroUsuarios) - gastoTotal 
utilidadesTotales = utilidadesActuales / utilidadesPasado

#MOSTRANDO LOS RESULTADOS

print ("Las Utilidades de este proyecto son: " ,  utilidadesActuales)
print("")

print ("Las Utilidades del año pasado fueron: " ,  utilidadesPasado) 
print("")

print ("La razon entre la utilidad de este año y la utilidad pasada es:" ,  utilidadesTotales) 



