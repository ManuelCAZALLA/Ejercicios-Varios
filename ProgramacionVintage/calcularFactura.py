UNIDADES = 1
PRECIO = 0

def informaItem(precio,unidades):
     item = []
     item.append(unidades)
     item.append(precio)
     return item

unidades = float (input ("Cantidad de unidades : "))
precio = float (input ("Introduce el precio unitario en euros : "))

totalUnidades = 0
precioTotal = 0

listaFactura = []

while unidades > 0 and precio > 0 :
    totalunitario = unidades * precio
    item = informaItem(precio,unidades)
    listaFactura.append(item)
    
    print (precio, "€", "X" ,unidades,"unidades", "=",totalunitario,"€")
    
    totalUnidades += unidades
    precioTotal += totalunitario
    
    unidades = float (input ("Introduce cantidad : "))
    precio = float (input ("Introduce el precio unitario en euros: ") )
    
for item in listaFactura:
    print(item[PRECIO],"€",item[UNIDADES],"unidades",item [PRECIO]* item[UNIDADES], "€")

print ("------------------")
print ("Total : ", precioTotal,"€")   
print ("Unidades : ",totalUnidades,"unidades")
