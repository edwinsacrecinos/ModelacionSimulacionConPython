#Ciclo While normal
numerosImpares = 0
numerosPares = 0

numero = int (input("Introduce tu número o presiona 0 para salir: "))

while numero != 0:
    if numero % 2 == 1:
        numerosImpares +=1
    else:
        numerosPares +=1
    numero = int (input("Introduce tu número o presiona 1 para salir: "))
    
print ("Cantidad de impares ", numerosImpares)
print ("cantidad de pares ", numerosPares)


#Ciclo While con ELSE
i = int(input("Ingresa un valor: "))

while i < 100:
    print("Menor a 100")
    i = int(input("Ingresa un valor: "))
else:
    print("Mayor a 100")
    