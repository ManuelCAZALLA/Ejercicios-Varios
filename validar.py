def validacion(mensaje):
    numero= input (mensaje)

    esValido = False
    while not esValido :

        if numero.isdigit ():
            numero = int (numero)
            esValido = True
        elif numero != "" and numero[0]== "_"  and numero[1:].isdigit():
            numero = int (numero) 
            esValido = True 
        else:    
            print (numero,"Debe ser un numero entero")
            numero=  input (mensaje)
    return numero
numero= validacion("Introduzca un numero : ")
numero2 = validacion("Introduzca otro numero : ")

suma = numero + numero2
resta = numero - numero2
multi = numero * numero2
division = round(numero / numero2,2)

print (numero, "+", numero2, "=",suma )
print(numero, "-", numero2, "=", resta )
print(numero, "x", numero2, "=",multi )
print(numero, "/", numero2, "=",division )

