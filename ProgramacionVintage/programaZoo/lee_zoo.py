from config import preciosE
    

fEntradas = open('transacciones.txt','r')

totalEntradas = 0


numEntradaBebe= 0
numEntradaNiño = 0
numEntradaAdulto =0
numEntradaJubilado = 0


linea = fEntradas.readline()

while linea != "" :
    entradas = linea.split(',')
    numEntradaBebe += int(entradas[0])
    totalEntradas += int (entradas[0])
    numEntradaNiño += int(entradas [1])
    totalEntradas += int (entradas[1])
    numEntradaAdulto += int(entradas [2])
    totalEntradas += int (entradas[2])
    numEntradaJubilado +=int( entradas[3])
    totalEntradas += int (entradas[3])
 
    linea = fEntradas.readline()
    
print ("Entradas Bebe....: {:3d} - {}".format(numEntradaBebe,numEntradaBebe * preciosE ['bebe']) ) 
print ("Entradas Niño....:  {:3d} - {}" .format(numEntradaNiño,numEntradaNiño * preciosE ['niño'] ))    
print ("Entradas Adulto..: {:3d} - {}".format(numEntradaAdulto,numEntradaAdulto * preciosE ['adulto']) )    
print ("Entradas Jubilado:{:3d} - {}" .format(numEntradaJubilado,numEntradaJubilado * preciosE ['jubilado']))

print("\nTotal: {:3d} - {:7.2f}".format(totalEntradas,
                                        numEntradaBebe * preciosE['bebe']+ numEntradaNiño * preciosE['niño']+\
                                            numEntradaAdulto * preciosE['adulto']+ numEntradaJubilado * preciosE['jubilado']))       