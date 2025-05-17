from biblioteca_ferreteria import *

while True:
    print("1- Reponer mercadería (productos existentes)")
    print("2- Vender mercadería (producto existente, solo si alcanza el stock)")
    print("3- Listar inventario")
    print("5- Salir")
    opcion=int(input("ingrese la opcion: "))

    if opcion==1:
        reponer_mercaderia(estanteria)
    elif opcion==2:
        vender_mercaderia(estanteria)
    elif opcion == 3:
        listar_inventario(estanteria)
    elif opcion== 5:
        break
    else:
        print("vuelve a ingresar una opcion: ")
    
