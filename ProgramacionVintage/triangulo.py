def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False


base = input("Base del triangulo : ")

while not esDecimal(base):
    print (base,"tiene que ser un numero")
    base = (input("Base del triangulo : "))

altura = input ("Altura de triangulo : ")

while not esDecimal(altura):
    print (altura,"tiene que ser un numero") 
    altura = input ("Altura de triangulo : ") 
    
b = float (base)
h = float (altura)
media = b * h / 2

print (" El area de su triangulo es : ", round (media,2))     
    