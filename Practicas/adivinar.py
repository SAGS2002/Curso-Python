import random


num=random.randint(1,100)

adiv=0
while num != adiv:
    adiv+=1
    print(adiv)
    if adiv == num:
        print("Acertaste el numero que pensaba la maquina!!!")
        break
    else:
        print("Numero equivocado")
print("==================================")
