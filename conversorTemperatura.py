class Termometro ():
    def __init__(self):
        self.__unidadMedida = 'C'
        self.__temperatura = 0
     
    def __conversor(self,temperatura,unidad) :
        if unidad == 'C':
         return "{}º F".format(temperatura * 9/5 + 32)
        elif unidad == 'F':
          return "{}º C".format((temperatura -32) * 5/9)
        else:
            return "Unidad Incorrecta"
        
    def __str__(self):
        return "{}º {}".format(self.__temperatura,self.__unidadMedida) 
    
    def unidadMedida(self,uniM = None)  :
        if uniM == None :
            return self.__unidadMedida 
        else :
            if uniM == 'F' or uniM == 'C':
                self.__unidadMedida = uniM
                
    def temp(self,temperatura = None) :
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura
            
    def mide(self,uniM = None):
        if uniM == None or uniM== self.unidadMedida:
            return self.__str__()
        else:
            if uniM == 'F' or uniM == 'C':
              return self.__conversor(self.__temperatura,self.__unidadMedida)
            else:
                return self.__str__() 
        
        
t = Termometro()
t.temp(32) 
t.unidadMedida('F')
print(t.mide('C'))                    