def pedir_numeros():
    #declara la lista
    #pide al usario ingresar un numero durante 10 iteraciones y lo valida
    lista =[0]*10
    for i in range(len(lista)):
        numero=int(input("ingrese un numero del 1 al 100: "))
        while numero <= 0 or numero >= 100:
            numero=int(input("ingrese un numero entre 1 al 100: "))
        lista[i]=numero
    return lista
print(pedir_numeros())