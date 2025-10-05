#Funciones del calculo tomando el parametro de la opcion seleccionada
def calculos(op):

    #Se inicializa la variable del resultado
    resultado=0

    #Ingreso de datos
    num1_str=input("Ingresar primera cantidad: ")
    #conversion de datos a float para operaciones de reales
    num1=float(num1_str)
    
    num2_str=input("Ingresar segunda cantidad: ")
    num2=float(num2_str)

    print("--------------------------------")
    match op:
        case 1: 
            #Operacion
            resultado=num1+num2
            #Imprecion del resultado
            print(f"El resultado de {num1} + {num2} = {resultado}")
        case 2:  
            resultado=num1-num2
            print(f"El resultado de {num1} - {num2} = {resultado}")
        case 3:  
            resultado=num1*num2
            print(f"El resultado de {num1} x {num2} = {resultado}")
        case 4:  
            resultado=num1/num2
            print(f"El resultado de {num1} / {num2} = {resultado}")
            
        case 5:  
            resultado=num1%num2
            print(f"El modulo(residuo) de {num1} / {num2} = {resultado}")
            
        case 6:  
            resultado=num1**num2
            print(f"El resultado de {num1} elevado a la {num2} = {resultado}")
            