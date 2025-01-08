def nota(cifra):
    '''Función que elimina cambia las comas de separación de decimales por puntos de una cifra y la convierte en un real.
    Parámetros:
        - cifra: Es una cadena con una cifra.
    Devuelve:
        Un real con la cifra de la cadena después de cambiar el separador de decimales por punto.
    '''
    try:
        cifra = cifra.replace(',', '.')
        return float(cifra)
    except ValueError:
        return 0.0  # Si no se puede convertir la cifra, devolvemos 0


def calificaciones(ruta):
    '''Función que preprocesa los datos contenidos en un fichero con formato csv y devuelve una lista de diccionarios donde las claves de los diccionarios son los datos de la primera fila y los valores los datos de cada línea del fichero.
    
    Parámetros:
        - ruta: Es una cadena con la ruta del fichero.
    Devuelve:
        Una lista de diccionarios donde cada diccionario contiene los datos de una linea del fichero (a excepción de la primera línea), usando como claves los datos de la primera línea.
    '''
    try:
        # Abrimos el fichero en modo lectura de manera segura
        with open(ruta, 'r') as f:
            lineas = f.readlines()
    except FileNotFoundError:
        print('El fichero no existe.')
        return []
    
    if not lineas:
        return []

    # Leemos las claves del primer elemento de la lista, eliminamos el cambio de línea y dividimos la cadena por el punto y coma.
    claves = lineas[0].strip().split(";")
    calificaciones = []

    # Recorremos las líneas del fichero (empezamos desde la segunda línea)
    for i in lineas[1:]:
        # Eliminamos el cambio de línea del final y dividimos la cadena por el punto y coma.
        valores = i.strip().split(";")
        
        # Verificar que el número de valores coincida con el número de claves
        if len(valores) != len(claves):
            print(f'Error en la línea: {i}. El número de valores no coincide con las claves.')
            continue
        
        # Creamos el diccionario para la línea actual
        alumno = {claves[j]: valores[j] for j in range(len(valores))}
        calificaciones.append(alumno)
    
    return calificaciones


def añadir_nota_final(calificaciones):
    '''Función que recibe una lista de diccionarios con las calificaciones de cada alumno en un curso, calcula la nota final del curso de cada alumno y la añade al diccionario del alumno.
    Parámetros:
        - calificaciones: Es una lista de diccionarios donde cada diccionario contiene los datos de un alumno (nombre, asistencia y notas de exámenes del curso).
    Devuelve:
        La lista de las calificaciones de los alumnos tras añadir a cada alumno de la lista su nota final del curso.
    '''
    def nota_final(alumno):
        '''Función que calcula la nota final del curso de un alumno.
        Parámetros:
            - alumno: Es un diccionario con las notas del alumno.
        Devuelve:
            El diccionario con los datos del alumno tras añadirle un nuevo par con la nota final del curso.
        '''
        # Manejo de los parciales con validaciones
        parcial1 = nota(alumno.get('Ordinario1', '')) if alumno.get('Ordinario1') else nota(alumno.get('Parcial1', ''))
        parcial2 = nota(alumno.get('Ordinario2', '')) if alumno.get('Ordinario2') else nota(alumno.get('Parcial2', ''))
        practicas = nota(alumno.get('OrdinarioPracticas', '')) if alumno.get('OrdinarioPracticas') else nota(alumno.get('Practicas', ''))

        # Asignamos las notas calculadas al alumno
        alumno['Final1'] = parcial1
        alumno['Final2'] = parcial2
        alumno['FinalPracticas'] = practicas
        alumno['NotaFinal'] = parcial1 * 0.3 + parcial2 * 0.3 + practicas * 0.4
        
        return alumno

    # Aplicamos la función nota_final a todos los alumnos
    return [nota_final(alumno) for alumno in calificaciones]


def aprobados_suspensos(calificaciones):
    '''Función que recibe una lista de diccionarios con las calificaciones de cada alumno en un curso, y devuelve la lista de aprobados y suspensos en el curso.
    Parámetros:
        - calificaciones: Es una lista de diccionarios donde cada diccionario contiene los datos de un alumno (nombre, asistencia y notas de exámenes del curso).
    Devuelve:
        - aprobados: Es una lista con los nombres de los alumnos aprobados.
        - suspensos: Es una lista con los nombres de los alumnos suspensos.
    '''
    aprobados = []
    suspensos = []

    for alumno in calificaciones:
        # Validación de la asistencia como porcentaje
        try:
            asistencia = int(alumno['Asistencia'].replace('%', '').strip())
        except ValueError:
            asistencia = 0  # Si no se puede convertir, asumimos que no cumplió con la asistencia mínima

        # Condición para aprobar
        if (asistencia >= 75 and alumno['Final1'] >= 4 and alumno['Final2'] >= 4 and 
            alumno['FinalPracticas'] >= 4 and alumno['NotaFinal'] >= 5):
            aprobados.append(f"{alumno['Apellidos']}, {alumno['Nombre']}")
        else:
            suspensos.append(f"{alumno['Apellidos']}, {alumno['Nombre']}")

    return aprobados, suspensos


# Llamada a las funciones de prueba
califs = calificaciones('calificaciones.csv')
califs_con_nota_final = añadir_nota_final(califs)
print(califs_con_nota_final)
aprobados, suspensos = aprobados_suspensos(califs_con_nota_final)
print('Lista de aprobados:', aprobados)
print('Lista de suspensos:', suspensos)
