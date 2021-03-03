#Creación de Tuplas
miTupla = (1,2,3,4,5)

#Imprimir tupla

print("General: ",miTupla)
print("Sola: ",miTupla[0])

print("Vertical")
for elemento in miTupla:
    print(elemento)
    
#Funciones de agragar y buscar

agregado1 = miTupla +(10,20)
agregado2 = miTupla * 3
print(agregado1)
print(agregado2)
print("Sus elementos: ", len(miTupla))

print ("Existe: ", 1 in miTupla)
print ("No existe: ", 100 not in miTupla)
