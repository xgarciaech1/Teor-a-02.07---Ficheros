def nuevo_telefono(cliente, nom_tel):
    '''
    Función que devuelve el teléfono de un cliente de un fichero dado.
    Parámetros:
        nom_tel: Es un fichero con los nombres y teléfonos de clientes.
        cliente: Es una cadena con el nombre del cliente.
    Devuelve:
        El teléfono del cliente guardado en el fichero o un mensaje de error si el teléfono o el fichero no existe.
    '''
    try:
        f = open(nom_tel, 'r')
    except FileNotFoundError:
        return('El fichero' + nom_tel + 'no existe!\n')
    else:
        diccionario = f.readlines()
        f.close()
        diccionario = dict([tuple(linea.split(',')) for linea in diccionario])
        if cliente in diccionario:
            return diccionario[cliente]
        else:
            return ('el cliente' + cliente + 'no existe')

def añadir_cliente(nom_tel, cliente, telefono):
    '''
    Función que añade el teléfono de un cliente de un fichero dado.
    Parámetros:
        nom_tel: Es un fichero con los nombres y teléfonos de clientes.
        cliente: Es una cadena con el nombre del cliente.
        telefono: Es una cadena con el teléfono del cliente.
    Devuelve:
        Un mesaje informando sobre si el teléfono se ha añadido o ha habido algún problema.
    '''
    try:
        f = open(nom_tel, 'a')
    except FileNotFoundError:
        return('El fichero' + nom_tel + 'no existe\n')
    else:
        f.write(cliente + ',' + telefono + '\n')
        f.close()
        return('Telefono añadido\n')


def quitar_telefono(nom_tel, cliente):
    '''
     Función que elimina el teléfono de un cliente de un fichero dado.
    Parámetros:
        nom_tel: Es un fichero con los nombres y teléfonos de clientes.
        cliente: Es una cadena con el nombre del cliente.
    Devuelve:
        Un mesaje informando sobre si el teléfono se ha borrado o ha habido algún problema.
    '''
    try:
        f = open(nom_tel, 'r')
    except FileNotFoundError:
        return('El fichero' + nom_tel + 'no existe')
    else:
        diccionario = f.readlines()
        f.close()
        diccionario = dict([tuple(linea.split(',')) for linea in diccionario])
        if cliente in diccionario:
            del diccionario[cliente]
            f = open(nom_tel, 'w')
            for nombre, telefono in diccionario.items():
                f.write(nombre + telefono)
            f.close
            return('El telefono se ha borrado\n')
        else:
            return ('el cliente' + cliente + 'no existe')

def fichero(nom_tel):
    import os
    if os.path.isfile(nom_tel):
        fitxero = input('el fichero' + nom_tel + 'existe. Quieres borrarlo?(B/E)')
        if fitxero == 'E':
            return 'no se ha creado nuevo fichero'
    f = open(nom_tel, 'w')
    f.close()
    return 'Se ha creado el fitxero\n'

def menu():
    print('1 - Consultar telefonos')
    print('2 - Añadir telefono')
    print('3 - Eliminar telefono')
    print('4 - Crear nuevo fichero')
    print('5 - Terminar')
    opcion = input('Introduzca el numero que quiras hacer: ')
    return opcion

def fichero():
    nom_tel = 'listin.txt'
    while True:
        opcion = menu()
        if opcion == '1':
            nombre = input('Escribe el nombre que quieres consultar: ')
            print(nuevo_telefono(nom_tel, nombre))
        elif opcion == '2':
            nombre = input('Escribe el nombre que quieres añadir: ')
            telefono = input('Ecribe el telefono que quieras añadir: ')
            print(añadir_cliente(nom_tel, nombre, telefono))
        elif opcion == '3':
            nombre = input('Escribe el telefono que quieras quitar: ')
            print(quitar_telefono(nom_tel, nombre))
        elif opcion == '4':
            print(fichero(nom_tel))
        else:
            break
    return
fichero()