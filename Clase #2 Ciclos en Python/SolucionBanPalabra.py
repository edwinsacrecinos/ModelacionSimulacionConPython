print("Manda tu mensaje igual o menor a 10 palabras")
print("para terminar el mensaje antes coloca mfinal")
finalmsj=""
for letra in range(1,11):
    print("Ingresa palabra No. ",letra)
    msj=input()
    if(msj!="tonto"):
        if(msj=="mfinal"):
            break
        else:
            finalmsj+=msj+" "
    else:
        continue
print(finalmsj)

