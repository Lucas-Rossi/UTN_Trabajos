def buscar_numero(lista:list,numero:int)->list:
    #recibe lalista por parametro y un numero especifico
    #verifica si elnumero especifico esta en la lista y retorna True si es asi
    for i in range(len(lista)):
        if numero == lista[i]:
            return True
            
print(buscar_numero([10,20,30,40,7,50,60],20))