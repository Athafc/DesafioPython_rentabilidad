# CREACION DE VARIABLES
 
precioSuscripcion = 0

numeroUsuarios = 0 

gastoTotal = 0

utilidadesProyecto = 0

# SOLICITANDO DATOS AL USUARIO

numeroUsuarios =int(input("Ingrese la cantidad de usuarios: \n")) 

precioSuscripcion = int(input("Ingrese el precio de la suscripción: \n"))

gastoTotal = int(input("Ingrese el gasto operacional: \n"))

# SOLUCION DEL PROBLEMA

utilidadesProyecto = (precioSuscripcion * numeroUsuarios) - gastoTotal 

#MOSTRANDO LOS RESULTADOS

print ("Las Utilidades de este proyecto son: " ,  utilidadesProyecto) 


