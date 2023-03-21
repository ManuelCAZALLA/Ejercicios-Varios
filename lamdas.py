from functools import reduce
lista = [1,3,-1,15,9]

listaDobles = map(lambda x: x*2,lista) # la lista me la multiplica por 2 cada numero

print( "Lambda" ,list(listaDobles))

listaPares = filter (lambda x : x % 2 == 0,lista) # me devuelve true o false , en este caso me devuelve una lista vacia xk no son pares

print ("Filter : ", list(listaPares))

sumaTodos = reduce (lambda x,y : x + y,lista)

suma100 = reduce(lambda x,y : x+y, range(101))

print ("Reduce : ", sumaTodos)
print ("Reduce :",suma100)

def retrocede (e): # recursividad
    print("{}, ".format(e), end="")
    if e  > 0 :
        retrocede (e-1)
        
#retrocede (10)

def sumatorio(n):
    if n > 0:
        return n + sumatorio(n-1)
    else:
        return 0
    
print(sumatorio(4))   
    

        