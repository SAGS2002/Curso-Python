#Importo las funciones de otro archivo para no sobrecargar este
import funcionesCalc as f

#funcion para ejecutar la calculador
def calc():
    #Inicializo la variaje de la opcion
    op=0
    #Bucle para ejecutar la calculadora hasta que el usuario quiera detenerla
    while op!=8:
        #Input para seleccionar la operacion
        op=int(input("Ingrese la opcion \n1)suma             2)resta            3)multiplicacion  4)division \n5)modulo(residuo)   6)exponente        7)Salir \n="))
        print("--------------------------------")
        #Swicht para hacer la operacion seleccionada
        match op:
            case 1:
                #Llamado de la funcion importada, añadiendo el parametro "opcion"
                f.calculos(op)
            case 2:
                f.calculos(op)   
            case 3:
                f.calculos(op)
            case 4:
                f.calculos(op)
            case 5:
                f.calculos(op)
            case 6:
                f.calculos(op)
            case 7:
                print("Gracias por usar")
                break
            case _:
                print("Opcion no valida")
        print("=================================================================")

#Llamado de la funcion calc
calc()