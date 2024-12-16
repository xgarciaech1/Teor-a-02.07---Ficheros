#Escribir una función que pida un número entero entre 1 y 10 y guarde en un 
#fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, 
#donde n es el número introducido.
def multiplicar():
    n = int(input('Dime un numero entre el 1 y el 10: '))
    fichero = 'tabla' + str(n) + '.txt'
    f = open(fichero, 'w')
    for i in range(1, 11):
        f.write(str(n) + 'x' + str(i) + '=' + str(n * i) + '\n')
    f.close
multiplicar()