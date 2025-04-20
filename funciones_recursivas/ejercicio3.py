def sumar_digitos(num):
    if num <=9:
        return num
    else:
        return (num%10 )+ sumar_digitos(num//10)
        
print(sumar_digitos(143))