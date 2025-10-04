#Funcion para calcular de horas a milisegundo
def horasMili(hora):
    #Se convierten las horas a minutos
    min=hora*60
    #Los minutos a segundos
    seg=min*60
    #Y los segundo a milisegundos
    mili=seg*1000
    print(f"En {hora} hora/s hay un total de {mili} milisegundos")

def minutsMili(min):
    #Los minutos a segundos
    seg=min*60
    #Y los segundo a milisegundos
    mili=seg*1000
    print(f"En {min} hora/s hay un total de {mili} milisegundos")

def segsMili(seg):
    #Los segundo a milisegundos
    mili=seg*1000
    print(f"En {seg} hora/s hay un total de {mili} milisegundos")


#Input para seleccionar el valor a transformar
opcion = int(input("Ingrese que que quiere convertir en milisegundos 1)horas 2)minutos 3)segundos:\n"))

#Swicht para cada opcion
match opcion:
    case 1:
        horas=int(input("Ingrese la cantidad de horas que desea convertir: "))
        #Llamado de cada funcion
        horasMili(horas)
    case 2:
        minuts=int(input("Ingrese la cantidad de minutos que desea convertir: "))
        minutsMili(minuts)
    case 3:
        segs=int(input("Ingrese la cantidad de segundos que desea convertir: "))
        segsMili(segs)
    case _: 
        print("Opción no válida")