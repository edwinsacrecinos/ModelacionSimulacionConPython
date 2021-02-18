#Definir y llamar una función
def separador():
    print("::::::::::::::::::::::::::::::::::::::::")
   
print("Comienzo aquí")
separador()
print("Termino aquí")

#Función VOID
def sumaVacia():
    print (10+11)
sumaVacia()

#Función Return
def sumaLlena():
    return 10*10
print(sumaLlena())

#Funciones con parámetros simples
def saludo(nombre, saludar):
    print (nombre,saludar)

#Llenado directo   
saludo("Edwin","Buenos días")
#llenado con variables
A = "Juan"
B="Buenas tardes"
saludo(A,B)


#Función con parámetro por omisión
def mensaje (nombre,mensaje="Buenas noches"):
    print (nombre,mensaje)
    
mensaje("edwin")

#Función con parámetro por palabra clave
def saludoPersonalizado (persona, dedicatoria):
    print (persona, dedicatoria)
    
saludoPersonalizado(persona="Marta",dedicatoria="Te quiero")   

#Función con parámetro Arbitrario
def listaCompra(*lista):
    print(lista)
    
listaCompra('Leche','huevos','carne','frijol')

#Función con parámetro desempacado
def calculadora(compra, descuento):
    return compra - descuento

blusaAzul = [1500,250]
print("su compra con descuento es: ", calculadora(*blusaAzul))

#Función con return avanzada
def juegoAdivinador(numero):
    if (numero == 7):
        return True
    else:
        return False

var = int(input("Dame tu número para adivinarlo: "))

if (juegoAdivinador(var)):
    print("Has ganado")
else:
    print("Has perdido")

#Función como parámetro
def hora (hr):
    return hr + 2

varhr= int(input("Ingrese su hora actual: "))
def cambioHorario (mes):
    print ("El mes:",mes,"se adelanto",hora(varhr),"horas")

cambioHorario("Enero")


    
