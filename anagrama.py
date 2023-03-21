
'''def esAnagramaEle(p1,p2):
    listaLetras = []
    if len(p1) != len (p2):
        return False
    for caracter1 in p1:
        pasaPorAqui = False
        for caracter2 in p2:
            if caracter1 == caracter2 :
               pasaPorAqui = True
               listaLetras.append(True)
        if not pasaPorAqui:       
          listaLetras.append(False)
    if False in listaLetras :
        return False
    else:
        return True      
                    
                
print(esAnagramaEle("amar","ramo"))  

def esAnagrama (p1,p2):
    return esAnagramaEle(p1,p2)and esAnagramaEle(p2,p1) 

print(esAnagrama("amar","ramo"))'''

# Es anagrama con diccionario
def cuentaCaracteres (cadena) :
    contador = dict()
    for caracter in cadena :
        if caracter in contador :
            contador [caracter] +=1
        else :
            contador [caracter] = 1
            return contador  

def esAnagramaDic(p1,p2) :
    dicts1 = cuentaCaracteres(p1)
    dicts2 = cuentaCaracteres(p2)
    
    return dicts1 == dicts2              
            
print (esAnagramaDic("amor","amar"))            
            
        
        
   