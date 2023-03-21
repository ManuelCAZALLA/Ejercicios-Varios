class Perro ():
    def __init__(self,nombre,edad,peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    def ladrar(self):
        if self.peso >= 8 :
           return ('Guau, Guau')
        else:
            return ('ay, ay')
        
    def __str__(self):
        return 'Soy el perro {}, edad: {}, peso : {}'.format(self.nombre,self.edad,self.peso)    
    
sisuka = Perro('Sisuka',6,15)
drako = Perro('Drako',4,7)
lola = Perro ('Lola', 3,2)

class PerroAsistencia(Perro): # Herencia
    def __init__(self, nombre, edad, peso,amo):
        Perro.__init__(self,nombre,edad,peso)
        self.amo = amo
        self.__trabajando = False
    
    def __str__(self):
      return  ('Perro asistencia de {}'.format(self.amo)) 
   
    def pasear(self):
        return ('Ayudo a {} ha pasear'.format(self.amo))
    
    def ladrar(self):
        if self.__trabajando :
            print ('sssshhh, no puedo ladrar')
        else:
            Perro.ladrar(self)     
    
    def trabajando(self,valor = None):
        if valor == None :
            return self.__trabajando
        else:
            self.__trabajando = valor
    
pumuki = PerroAsistencia('Pumuki',19,5,'Loli')   

pumuki.trabajando(True)
print(pumuki.ladrar())   
       
     
