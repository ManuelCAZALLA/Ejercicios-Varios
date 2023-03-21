def clear ():
   print ("\033[2J]") # limpiar pantalla

def locate (line,column):
   print ("\033[{};{}H]".format(line,column),end="") # dejar el cursor en ese punto
   

