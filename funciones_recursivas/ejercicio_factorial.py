def calcular(num):
    if num==0:
        return 1
    else:
        return num*calcular(num-1)
print(calcular(6))