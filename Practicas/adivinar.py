import random


num=random.randint(1,100)

adiv=0
while num != adiv:
    
    adiv=int(input("Ingrese numero: "))
    if adiv == num:
        print("Acertaste el numero que pensaba la maquina!!!")
        break
    elif adiv >100:
        print("Numero no valido debe ser del 1-100")
    else:
        print("Numero equivocado")
print("==================================")
