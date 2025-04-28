def pedir_nombres():
    #se declara la lista y la cantidad de elementos
    #se itera segun la cantidad de elementos
    #se guarda el nombre en la posicion de la lista
    lista=[0]*10
    for i in range(len(lista)):
        nombre=input("ingrese un nombre: ")
        lista[i]=nombre
        
    return lista

print(pedir_nombres())
