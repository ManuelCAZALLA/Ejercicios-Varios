def imprimeCosas(*listaDeCosas) :
    for item in listaDeCosas :
        print (item)
        
imprimeCosas('movil','cargador','funda','auriculares') 


def imprimeDiccionario(**diccionariodeparametros) :
    if 'line' in diccionariodeparametros :
        print('Posicionar en linea',diccionariodeparametros['line'])
    else:
        print ('No existe line')          


imprimeDiccionario(contenido = 'la cosa',line = 5)
