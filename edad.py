nombre = input ("Dime tu nombre : ")
edad = int (input ("¿Cuantos años tienes? : "))
anoActual = int (input ("¿En que año estamos : ?"))
mes = int (input (" ¿En que mes estamos?"))
dia = int (input ("¿En que dia estamos?"))
transcurridos = 0
i = 0

diasMes = [31,28,31,30,31,30,31,31,30,31,30]

while i < mes -1 :
  transcurridos = transcurridos + diasMes[i]
  i = i + 1
  
transcurridos = transcurridos + dia
  
prob = transcurridos / 365 * 100
nacimiento = anoActual - edad

print (nombre," naciste en el", nacimiento, "con una probabilidad de ", prob) 
print ("o en ", nacimiento - 1, "con una probabilidad de ",100 - prob)                         
                      
      
      
      
    

