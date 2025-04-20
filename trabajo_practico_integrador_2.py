sigue=True
elite_plano_adulto=0
flag= True
jugadores=0
saque_mas_usado_plano=0
saque_mas_usado_cortado=0
saque_mas_usado_liftado=0
experto = 0
promedio =0
veces =0
el_menor=0
nombre=""
categoria=""
while sigue:
    nombre_del_jugador=input("ingrese el nombre del jugador: ")
    edad=int(input("ingrese la edad del jugador: "))
    while edad <8:
        edad=int(input("ingrese la edad del jugador: "))
    cantidad_de_puntos=int(input("ingreselos punto del jugador: "))
    while cantidad_de_puntos < 0 or cantidad_de_puntos > 60:
        cantidad_de_puntos=int(input("ingreselos punto del jugador: "))
    numero_de_partidos_ganados=int(input("ingrese el numero de partidos ganados: "))
    while numero_de_partidos_ganados <0 or numero_de_partidos_ganados > 35:
        numero_de_partidos_ganados=int(input("ingrese el numero de partidos ganados: "))
    tipo_de_saque=input("ingrese un tipo de saque: plano, liftado, cortado: ")
    categoría_del_jugador=input("ingrese la categoria: elite, experto, avanzado: ")
    jugadores +=1

    if categoría_del_jugador == "elite":
        if tipo_de_saque == "plano":
            saque_mas_usado_plano+=1
            if edad > 19 and edad <= 25:
                elite_plano_adulto +=1
        elif tipo_de_saque=="liftado":
            saque_mas_usado_liftado+=1
        else:
            saque_mas_usado_cortado+=1

    elif categoría_del_jugador == "experto":
        experto +=1

    elif categoría_del_jugador=="avanzado":
        promedio += edad
        veces +=1

    if cantidad_de_puntos > 50:
        if flag == True:
            el_menor=edad
            nombre=nombre_del_jugador
            categoria=categoría_del_jugador
            flag=False
        elif el_menor > edad:
            el_menor=edad
            nombre=nombre_del_jugador
            categoria=categoría_del_jugador
    decicion=input("hay que agregar otro jugador?: s/n")
    if decicion == "n":
        sigue = False
    

print(f"los jugadores elites con saque plano entre 19 y 25 de edad son: {elite_plano_adulto}")
print(f"el jugador con mas de 50 puntos y mas joven es: {nombre} con {el_menor} y su categoria es {categoria}")
print("el porcentaje de jugadores experto es: ",(experto/jugadores)*100)
print("el promedio de edad de los jugadores avanzados es: ",(promedio / veces))
if saque_mas_usado_plano > saque_mas_usado_cortado and saque_mas_usado_plano > saque_mas_usado_liftado:
    print("el saque mas usado es el plano")
elif saque_mas_usado_cortado>saque_mas_usado_plano and saque_mas_usado_cortado > saque_mas_usado_liftado:
    print("el saque mas usado es el cortado")
else:
    print("el saque mas usado es el liftado")
