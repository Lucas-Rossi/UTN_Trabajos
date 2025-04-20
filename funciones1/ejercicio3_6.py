def solicitar_valor():
    #solicita un valor y lo valida entre 10 y 100
    numero1=int(input("ingrese un valor entre 10 y 100: "))
    while numero1 <10 or numero1 > 100:
        numero1=int(input("ingrese un valor entre 10 y 100: "))
    return numero1

def realizar_descuento(numero1:int):
    #realiza un descuento y muestra el precio total
    descuento= numero1 * 0.05
    precio_total=numero1-descuento
    print("tu descuento es de: ",descuento)
    print("tu precio total es de: ",precio_total)

realizar_descuento(solicitar_valor())