#Condicionales 
print("Uso de las condicionales: ")
valor = int(input("Ingresa tu número: "))
#menor y mayor
print (valor<100)
print (valor>100)
#menor o igual y mayor o igual
print (valor >= 100 )
print (valor <= 100)
#igual igual
print (valor == 100)
#diferente
print (valor != 100)


#USO DEL IF
print ("Comparemos números: ")
if valor > 200:
    print ("Es Cierto")
else: 
    print ("No es Cierto")
print ()
#USO DEL ELIF
if valor < 200:
    print("es menor")
elif valor > 200:
    print ("Es mayor")
elif valor == 200:
    print ("Es igual")
else:
    print ("No paso nada")   