import os
n = int(input('dime un numero del 1 al 10: '))
fichero = 'tabla' + str(n) + '.txt'
try: 
    f = open(fichero, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    print(f.read())
    f.close()