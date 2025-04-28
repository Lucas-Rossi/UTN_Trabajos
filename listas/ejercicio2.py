def editar_lista():
    #se crea una lista con 10 elementos iniciados en 0
    #se pide al usario que ingrese un numero que quiera agregar y la posicion de dicho numero
    #pregunta al usario si quiere agregar mas numeros en caso contrario retorna la lista
    lista=[0]*10
    continuar="s"
    for i in range(len(lista)):
        print(lista[i])
    
    while continuar == "s":
        numero=int(input("ingrese el numero que quiere agregar: "))
        posicion=int(input("ingrese la posicion del numero que quiere cambiar: "))
        lista[posicion]=numero
        continuar=input("quiere seguir? s/n: ")
    return lista

print(editar_lista())
    
    