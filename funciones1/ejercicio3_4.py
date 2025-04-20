def pedir_retornar_numero():
    #pedir el ingreso de un numero que lo retorne y lo muestre por panatlla
    #valida el número en un rango pasado por parámetro “desde”-“hasta”
    desde=int(input(f"ingresar numero minimo: "))
    hasta=int(input(f"ingresar numero maximo: "))

    while hasta < desde:
        hasta=int(input(f"ingresar numero maximo: "))

    numero = int(input(f"ingresar numero desde{desde} hasta {hasta}: "))
    
    while numero < desde or numero > hasta:
        numero = int(input(f"ingresar numero desde{desde} hasta {hasta}: "))

    print("el numero es:",numero)
    return numero

pedir_retornar_numero()