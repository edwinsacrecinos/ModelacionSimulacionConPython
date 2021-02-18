#funciono compleja factoriales
def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    producto = 1
    for i in range(2, n + 1):
        producto *= i
    return producto

print("Calcular el factorial de tu rango:")
inicio = int(input("Ingresa el inicio: "))
final = int (input("Ingresa el final: ")) +1 #esto recordando como cuenta el range

for n in range(inicio, final): # probando
    print("Factorial de:",n,"es:", factorialFun(n))