gondola=[["vacio",["botellas",3],"vacio",["frascos",8],"vacio"],
         ["vacio","vacio",["fideos",4],"vacio","vacio"],
         ["vacio","vacio","vacio",["leche",6],"vacio"]]

def agregar_producto(gondola:list)->list:
    x=int(input("ingrese la fila: "))
    y=int(input("ingrese la columna: "))    
    if gondola[x][y]=="vacio":
        producto=input("que producto quieres agregar?: ")
        cantidad=int(input("ingrese la cantidad: "))
        gondola[x][y] = [producto,cantidad]
    else:
        print("ese producto ya existe")

def baja_de_productos(gondola:list):
    x=int(input("ingrese la fila del producto al que quiere dar de baja: "))
    y=int(input("ingrese la columna del producto al que quiere dar de baja: "))
    if gondola[x][y]=="vacio":
        print("no hay ningun producto al que dar de baja.")
    else:
        print(f"en esa posicion se encontraba {gondola[x][y]}")
        gondola[x][y]="vacio"
        print(f"ahora esa posicion esta {gondola[x][y]}")

def modificar_producto(gondola:list):
    x=int(input("ingrese la fila: "))
    y=int(input("ingrese la columna: "))
    if gondola[x][y] != "vacio":
        print(gondola[x][y])
        producto=input("que producto quieres modificar?: ")
        cantidad=int(input("ingrese la cantidad: "))
        gondola[x][y] = [producto,cantidad]
        ubicacion=(input("quiere tambien cambiar la ubicacion del producto? s/n"))
        if ubicacion == "s":
            nueva_fila=int(input("ingrese la fila a la que quiere reubicar el producto: "))
            nueva_columna=int(input("ingrese la columna a la que quiere reubicar el producto: "))
            aux=gondola[nueva_fila][nueva_columna]
            gondola[nueva_fila][nueva_columna]= [producto,cantidad]
            gondola[x][y]=aux
    else:
        print("vacio")
        print("no puedes modificar un lugar que no hay nada, debes seleccionar la opcion para dar de alta primero")

def listar_productos(gondola: list):
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    producto_nuevo = [nombre, cantidad]

    for i in range(len(gondola)):
        for j in range(len(gondola[i])):
            if gondola[i][j] == "vacio":
                gondola[i][j] = producto_nuevo
                print(f"Producto '{nombre}' agregado en la posición ({i}, {j})")
                return

    print("No hay lugar vacío para agregar el producto.")

def ordenar_lista_por_nombre(gondola:list):
    lista=[]
    for i in range(len(gondola)):
        for j in range(len(gondola[i])):
            if gondola[i][j] != "vacio":
                lista.append(gondola[i][j])
    
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if(lista[i][0] > lista[j][0]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

    indice = 0
    for i in range(len(gondola)):
        for j in range(len(gondola[i])):
            if gondola[i][j] != "vacio":
                gondola[i][j] = lista[indice]
                indice += 1
    