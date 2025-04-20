def solicitar_numero_entero():   
    numero=int(input("ingrese un numero entero"))
    while numero<0:
        numero=int(input("ingrese un numero entero"))
    return numero