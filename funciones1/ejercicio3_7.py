def restar(num1:int, num2:int):   
    resultado = num1 - num2
    return resultado

def sumar(num1:int, num2:int):
    resultado = num1 + num2
    return resultado

def calcular_valores():
    #pide al usario un valor para las variables numero 1 y numero 2
    #los valida entre 10 y 100
    #pide ingresar un operador y segun la eleccion del usuario suma o resta
    numero1=int(input("ingrese el primer valor entre 10 y 100: "))   
    while numero1 <10 or numero1 > 100:
        numero1=int(input("ingrese un valor entre 10 y 100: "))

    numero2=int(input("ingrese el segundo valor entre 10 y 100: "))
    while numero2 <10 or numero2 > 100:
        numero2=int(input("ingrese un valor entre 10 y 100: "))

    operacion=input("ingrese 's' para sumar  o  'r' para restar: ")
    while operacion != "s" and operacion != "r":
        operacion=input("ingrese 's' para sumar  o  'r' para restar: ")
    
    if operacion == "s":
        print(sumar(numero1,numero2))
        
    else:
        print(restar(numero1,numero2))
    
calcular_valores()

