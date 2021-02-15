import time

#For de 1 variable
print("For con 1 variable")
for i in range (10): #Los recorridos e indices inician en 0
    print("El valor de variable es: ", i)

#For de 2 variables
Print("For con 2 variables")
for j in range (1,11):
    print("El valor de variable es: ", j)

#For con 3 variables
print("for con 3 variables")
for x in range (0,12,2):
    print("El valor de variable es: ", x)

#For con continue
print("for con continue")
for x in range (0,12,2):
    if x == 8:
        continue
    print("El valor de variable es: ", x)

#For con break
print("for con break")
for y in range (1,11):
    if y == 5:
        break
    print ("La variable sigue dentro del ciclo: ",y)

#For con tiempo de espera
print ("For con tiempo de espera: ")
tiempo = int (input("Ingresa el tiempo por persona: "))
fila = int (input("Ingrese cantidad de personas: "))
filaArreglada = fila + 1 
for f in range (1, filaArreglada):
    print ("cliente número: ", f , " Atendido")
    time.sleep(tiempo)
print ("Todos los clientes atendidos")
    
