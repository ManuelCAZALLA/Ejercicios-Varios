# funciones de primer grado me suma los 100 primeros y el cuadrado

def normal(x) :
    return x

def cuadrado(x):
    return x * x
    
def cubo (x):
    return x ** 3    
    

def sumaTodos(limitTo,f):
    resultado = 0
    for i in range (limitTo+1) :
        resultado += f(i)
    return resultado    
    
print (sumaTodos(100,normal) ) 
print (sumaTodos(3, cuadrado))
print (sumaTodos(3,cubo))

# funciones que devuelven el max , el min y la media de una lista que le metamos


def maxi (*l) :
    if len(l) == 0 :
        return 0
    max = l[0] 
    for i in range (1,len(l)) :
        if l[i] > max :
            max = l[i]
    return max    
            
print (max(1,10,2,32))

def mini(*l): 
    if len(l) == 0 :
        return 0
    min = l[0] 
    for i in range (1,len(l)) :
            if l[i] < min :
                min = l[i]
    return min 

print (min(0,3,-5,10)) 

def media(*l) :
    if len(l) == 0 :
        return 0
    suma = 0
    for valor in l :
        suma += valor
    return suma / len (l)

funciones = {
    'max ': maxi,
    'min' : mini,
    'med' : media
}
 

def returnF(nombre):
    
   if nombre in funciones.keys() :
        return funciones[nombre]
   
   return None



          