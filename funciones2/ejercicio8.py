def numeros_primos(numero):
    contador=0
    primos=0
    for i in range(1,numero+1):
            contador =0

            for j in range(1, i+1):           
                if i % j==0:
                    contador+=1    

            if contador == 2:  
                print("primos: ",i)
                primos +=1
    return primos            


numeros_primos(19)