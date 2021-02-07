#El reto del if 
''' (comentario multilinea)
El ejercicio consiste en pedir si suma, resta o 
multiplicación y realizar la operación, usando IF 
'''
print("Qué tipo operación deseas hacer")
print("Suma = s, Resta = r, multiplicación = m")
cadena = input()
var1 = int (input("Ingrese el valor 1: "))
var2 = int (input("Ingrese el valor 2: "))
if cadena == "s":
    print ("La suma es: ")
    print (var1 + var2)
elif cadena == "r":
    print ("La resta es: ")
    print (var1 - var2)
elif cadena == "m":
    print ("La multiplicación es: ")
    print (var1 * var2)