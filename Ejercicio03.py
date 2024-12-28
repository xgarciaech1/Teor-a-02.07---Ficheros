#Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero
#tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla
#la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por
#pantalla informando de ello.
'''import os 
n = int(input('Dime un numero entre el 1 y el 10: '))
m = int(input('Dime otro numero entre el 1 y el 10: '))
fichero = 'tabla' + str(n) + '.txt'
if os.path.exists(fichero):
    with open(fichero, 'r') as archivo:
        lineas = archivo.redline()
    if 0 < m <= len(lineas):
        print(lineas[m - 1])
    else:
            print(f'La tabla no tiene una línea {m}')
else:
    print(f'No existe el fichero con la tabla del {n}') '''
n = int(input('Introduce un número entero entre 1 y 10: '))
m = int(input('Introduce otro número entero entre 1 y 10: '))
fichero = 'tabla' + str(n) + '.txt'
try: 
    with open(fichero, 'w') as f:
        lineas = f.readlines()
    print(lineas[m - 1])
except FileNotFoundError:
    print('No existe el fichero con la tabla del ', n)
          