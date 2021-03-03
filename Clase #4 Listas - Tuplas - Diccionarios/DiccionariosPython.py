#DICCIONARIOS

#Diccionarios Directos

#dict={"animal1" : "Gato", "animal2":"perro"}
#print(dict['animal1'])

#Diccionario Estilo Variable

agendaTelefonica ={'Carlos': 25304550, 'Claro':147100,'Marta': 78996000}
print(agendaTelefonica)
print(agendaTelefonica['Claro'])

#Diccionario vacío
diccionarioVacio={}

#Diccionario Vertical

agendaTelefonica2 ={
    "Juan": 25304550, 
    "Claro": 147100,
    "Luisa": 78996000
    }

#Recorrido de diccionario con Keys

dict = {"gato":"cat","perro":"dog","agua":"water"}

for key in dict.keys():
    print(key, "->", dict[key])
    
#Recorrer valores

for valores in dict.values():
    print (valores)
        
#Recorrer diccionario ordenado

for llave in sorted(dict.keys()):
    print (llave, "->",dict[llave])
    
#Impresión en conjunto

for espaniol, ingles in dict.items():
    print (espaniol, "->",ingles)

#Agregar items al diccionario

print("diccionario antiguo", dict)
dict['Amarrillo']= 'yellow'
print("diccionario nuevo", dict)

