#Suma los primeros 100 numeros

'''sumaTotal = 0
contador = 0

while contador <= 100:
    sumaTotal += contador
    contador+=1
print  (sumaTotal)''' 

'''sumaTotal = 0


for contador in range (1,101):
    sumaTotal+= contador
    print(sumaTotal)'''
# Calcular media de una lista    
notas = (1,2,9,7)   



 
indice = 0
suma = 0
while indice < len(notas):
    suma= suma + notas[indice]
    indice+=1
 

# Calcular media
media = suma/indice

print ("La lista tiene ",indice,"items") 
print ("Nota total :",suma)  
print ("La media es :", media) 

# Calcular media de una lista con for

'''notas = (1,2,9,7)   

def contenido (lista,indice):# con esta funcion controlo que haya algo en la lista
    try:
        resultado = lista[indice]
    except:
       resultado = None
        
    return resultado 

def longitud (lista):
    indice = 0
    while contenido(lista,indice) != None:
        indice+=1
    return indice    

longitudNotas = longitud(notas) # LLamo a la funcion en una variable para que no se repita tanto el ciclo        
suma = 0
for indice in range (0,longitudNotas):
    suma = suma + notas[indice]  
    
media = suma / longitudNotas

print ("La lista tiene ",longitudNotas,"items") 
print ("Nota total :",suma)  
print ("La media es :", media)'''

#  Calcular media mas simple

'''notas = (1,2,9,7)   

suma = 0
longNotas = len(notas)
for i in range (0,longNotas):
    suma = suma + notas[i]
    
media = suma / longNotas 

print ("La lista tiene ",longNotas,"items") 
print ("Nota total :",suma)  
print ("La media es :", media)'''          
 
    
     

