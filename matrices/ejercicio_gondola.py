from biblioteca_gondola import *

while True:
    for i in range(len(gondola)):
        for j in range(len(gondola[i])):
            print(gondola[i][j])
    print("1-Alta de productos (producto nuevo )")       
    print("2-Baja de productos (producto existente) ")
    print("3-Modificar productos cantidad, ubicación ")
    print("4-Listar productos ")
    print("5-Lista de productos ordenado por nombre ")
    print("6-Salir")
    opcion=int(input("seleccion una opcion: "))
    if opcion==1:
        agregar_producto(gondola)
    elif opcion == 2:
        baja_de_productos(gondola)
    elif opcion==3:
        modificar_producto(gondola)
    elif opcion== 4:
        listar_productos(gondola)
    elif opcion==5:
        ordenar_lista_por_nombre(gondola)
    elif opcion==6:
        break
    else:
        print("opcion no valida")




    







