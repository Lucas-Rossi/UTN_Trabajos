estanteria = [
    [["to12", 65], ["to16", 86], ["to20", 65], ["to25", 45]],
    [["to30", 68], ["to35", 73], ["to40", 85], ["to45", 89]],
    [["ta4", 58], ["ta5", 48], ["ta6", 64], ["ta7", 96]],
    [["ta8", 36], ["ta10", 72], ["ta12", 78], ["ta14", 71]]
]

def reponer_mercaderia(estanteria:list):
    x=int(input("ingrese la fila: "))
    y=int(input("ingrese la columna: "))
    cantidad=int(input("ingrese la cantidad a reponer"))
    estanteria[x][y][1]+=cantidad
    print(f"la cantidad es:",estanteria[x][y][1])

def vender_mercaderia(estanteria):
    x=int(input("ingrese la fila: "))
    y=int(input("ingrese la columna: "))
    cantidad=int(input("ingrese la cantidad a vender"))
    if estanteria[x][y][1] >= cantidad:
        estanteria[x][y][1] -= cantidad
        print(f"haz vendido {cantidad} {estanteria[x][y][0]}, y quedan {estanteria[x][y][1]} {estanteria[x][y][0]}")
    else:
        print("stock insuficiente")

def listar_inventario(estanteria):
    for i in range(len(estanteria)):
        for j in range(len(estanteria[i])):
            print(estanteria[i][j])