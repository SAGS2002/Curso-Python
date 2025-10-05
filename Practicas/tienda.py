listaItems={}
listaPrices={}
cant={}
total=0
iva=0.06
rep=int(input("Ingrese cantidad de articulos que va a comprar: "))


for i in range(0,rep):
    precio=0
    cantidad=0
    listaItems[i]=input("Ingrese nombre del producto: ")
    precio=float(input("Ingrese precio del producto: "))
    listaPrices[i]=precio
    
    cantidad=int(input("Ingrese cantidad del producto: "))
    cant[i]=cantidad
    total+=precio*cantidad

print(f"Num Nombre  Precio  cantidad")



for i in listaItems:
    print(f"{i+1} {listaItems[i]} {listaPrices[i]*cant[i]}$ {cant[i]}")

print(f"Total{(total*iva)+total}")