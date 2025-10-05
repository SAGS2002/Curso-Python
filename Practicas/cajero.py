def cajero():
        op=0
        fondo=0
        fondos=float(fondo)
        while op!=4:
            op=int(input("Ingrese la operacion que desea realizar \n 1) consultar 2)Depositar 3)Retirar 4)Salir \n ="))
            print("--------------------------------------------------------------------------")       
            match op:
                case 1:
                    print(f"Los fondos en su cuenta son de {fondos}$")
                case 2:
                    fondoIngStr=input("Ingrese la cantidad que desea guardar: ")
                    fondoIng=float(fondoIngStr)
                    print(f"Se añadieron {fondoIng}$ a la cuenta")
                    fondos=fondos+fondoIng
                case 3:
                    fondoRetStr=float(input("Ingrese la cantidad que desea retirar: "))
                    fondoRet=float(fondoRetStr)
                    if fondoRet>fondos:
                        print("Fondos en la cuenta insuficientes para retirar")
                    else:
                        print(f"Se retiraron {fondoRet}$")
                        fondos=fondos-fondoRet
                case 4:
                    print("Vuelva Pronto")
                case _:
                    print("Opcion no valida")
            print("===========================================================================")

cajero()