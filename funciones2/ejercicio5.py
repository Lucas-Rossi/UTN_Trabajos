def mostrar_numero_mas_grande(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    else:
        print(num3)

mostrar_numero_mas_grande(190,28,700)