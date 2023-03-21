numero1=  (input ("Introduzca un numero : "))

esValido = False

while not esValido :

    if numero1.isdigit ():
        numero1 = int (numero1)
        esValido = True
    elif numero1 != "" and numero1[0]== "_"  and numero1[1:].isdigit():
        numero1 = int (numero1) 
        esValido = True 
    else:    
        print (numero1,"Debe ser un numero entero")
        numero1=  (input ("Introduzca un numero : "))

numero2= (input ("Introduzca otro numero : "))        

esValido2 = False      
while not  esValido2 :    
        if numero2.isdigit():
            numero2 = int (numero2)
            esValido2 = True
        elif numero2 != "" and numero2[0]== "-"  and numero2[1:].isdigit():
            numero2 = int (numero2) 
            esValido2 = True     
        else:    
            print (numero2,"Debe ser un numero entero")
            numero2=  (input ("Introduzca otro numero : "))

numero1 = numero1/10
numero2 = numero2/10


suma = numero1 + numero2
resta = round(numero1 - numero2,2)
multi = numero1 * numero2
division = round (numero1 / numero2,2)

print (numero1, "+", numero2, "=",suma )
print(numero1, "-", numero2, "=", resta )
print(numero1, "x", numero2, "=",multi )
print(numero1, "/", numero2, "=",division )






