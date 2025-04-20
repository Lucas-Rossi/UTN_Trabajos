def verificar_primo():
    numero=int(input("ingrese un numero:"))
    divisor=0

    for i in range(1,numero):
        if numero % i == 0:
            divisor+=1
    if divisor<= 2:
        valor=True
    else:
        valor=False
    return valor

print(verificar_primo())