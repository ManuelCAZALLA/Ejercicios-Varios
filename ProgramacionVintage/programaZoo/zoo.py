import screen
from config import preciosE,entradasQ


numEntradas = {"bebe": 0,"niño":0,"adulto": 0, "jubilado": 0}



def tipoEntrada(edad):
    if edad > 0 and edad <= 2:
        tipo = "bebe"
    elif edad <= 12 :
        tipo = "niño"
    elif edad < 65 :
        tipo = "adulto"
    else :
        tipo = "jubilado"
        
    return tipo               
        
def validaEdad(cadena):
    try:
       n = int (cadena)
       if n >= 0 :
           return True
       return False
    except :
        return False    

def pedirEdad():
    screen.locate(1,1)
    edad = (input ("¿Que edad tienes? : "))
    while validaEdad(edad)== False :
        print ("Edad invalida")
        screen.locate(1,1)
        edad = int (input ("¿Que edad tienes? : "))
    return  int (edad)

def printScreen():
    screen.locate(4,5)
    print("Bebe....:  -")
    screen.locate(5,5)
    print("Niño....:  -")
    screen.locate(6,5)
    print ("Adulto..:  -")
    screen.locate(7,5)
    print("Jubilado:  -")
    
    screen.locate(9,8)
    print ("Total....:")
    

screen.clear()
printScreen()        

def main():
    edad = pedirEdad()
    precioTotal = 0

    while edad != 0 :
        tipoE = tipoEntrada(edad)
        precioE = preciosE[tipoE]
        numEntradas[tipoE]+= 1
        screen.locate(entradasQ[tipoE]['cantidad'][0],entradasQ[tipoE]['cantidad'][1])
        print(numEntradas[tipoE])
        screen.locate(entradasQ[tipoE]['precioA'][0],entradasQ [tipoE] ['precioA'][1])
        print( "{:7.2f}€".format(numEntradas[tipoE]* precioE))
        
        precioTotal += precioE
        screen.locate(9,19)
        print("{:7.2f}€".format(precioTotal))
        
        edad = pedirEdad()
        
    fEntradas = open('transacciones.txt','a+') 
    transaccion = "{},{},{},{}\n".format(numEntradas['bebe'],numEntradas['niño'],numEntradas['adulto'],numEntradas['jubilado'])
    fEntradas.write(transaccion)
    fEntradas.close()
    screen.locate(11,1) 
    
main()       
    
