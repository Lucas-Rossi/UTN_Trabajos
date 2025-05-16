mapa = [
 [0, 0, 0, 0, 0],
 [0, 0, 0, 1, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0] ]

def verificar_tesoro(mapa: list, x: int, y: int) -> int:  
    x_tesoro=0
    y_tesoro=0
    for i in range(len(mapa)):
            for j in range(len(mapa[i])):
                if mapa[x][y]==1:
                    x_tesoro=mapa[x]
                    y_tesoro=mapa[y]
                    
    if mapa[x][y]==1:
        distancia=0
        print("encontraste el tesoro")
    elif mapa[x][y]==0:
         distancia = x - x_tesoro + y - y_tesoro
         print(f"Fallaste. El tesoro está a {distancia} casilleros de distancia: ", )        
    return distancia
seguir="s"
while seguir =="s":
    x=int(input("ingrese un una cordenada x entre 0 y 4: "))
    y=int(input("ingrese una cordenada y entre 0 y 4 : "))
    while x < 0 or x>4 and y < 0 or y >4 :
        x=int(input("ingrese un una cordenada x entre 0 y 4: "))
        y=int(input("ingrese una cordenada y entre 0 y 4 : "))

    verificar_tesoro(mapa, x, y)

    seguir=input("quiere seguir jugando s/n")

        

