def determinar_primo(num,div):
    flag= True
    if div == 1:
        return flag
    elif (num%div)==0:
        flag=False
        return flag               
    else:
        return  determinar_primo(num, div - 1)
    

numero=int(input("ingrese un numero: "))    
divisor=numero-1
resultado=determinar_primo(numero,divisor)


if resultado==True:
    print("es primo",numero)
else:
    print("no es primo",numero)