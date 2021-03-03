#Listas/Vectores

numeros=[1,2,3,4,5] #El indice se inicia a contar de 0
letras=["a","b","c","d","e","f"]
valores=[True,False] 

#Imprimir Lista y contar su contenido

#print(letras)
#print (letras[0])
#print("La cantidad es: ",len(numeros))

#Agregar elementos en la última posición

#print("Lista Antigua: ",letras)
#letras.append("g")
#print("Lista Nueva: ",letras)

#Agregar elemento en cualquier posición

#print("Lista Antigua: ",numeros)
#numeros.insert(0,0) #El primer dato es la posición y el según lo que inserto
#print("Lista Nueva: ",numeros)

#Lista Vacía y su llenado

#miListaVacia = []
#for i in range (5):
#    miListaVacia.append(i+1)
#print(miListaVacia)

#Recorrido con For en Lista

#listaNumerica=[10,20,30,40,50]
#sumaNumeros=0
#for i in range(len(listaNumerica)):
#    print(i)
#    sumaNumeros += listaNumerica[i]
#print("Resultado total: ",sumaNumeros)

#Evaluar sí hay un elemento en la lilsta

listaFechas = [2000,2020,2021,2005]

#Sí está  

print(2000 in listaFechas) # Sí está es igual a True
print(1994 in listaFechas) #No está es igual a False

#No está 

print(2021 not in listaFechas) # Sí está es igual a False
print(1995 not in listaFechas) #No está es igual a True

#Cambiar valores o moverlos
#cambiar valor
listaAnios= [20,15,30,40,50]
print(listaAnios)
print("Lista con elementos cambiados")
listaAnios[0] = listaAnios [4]
print(listaAnios)
#mover el valor
print("Lista con elementos movidos")
listaAnios[1], listaAnios[2] = listaAnios[2], listaAnios[1]
print(listaAnios)