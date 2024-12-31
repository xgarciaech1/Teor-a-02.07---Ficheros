#Escribir un programa que abra el fichero con información sobre el PIB per
#cápita de los países de la Unión Europea
#( https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true ),
#pregunte por las iniciales de un país y muestre el PIB per cápita de ese país
#de todos los años disponibles
def parsear_pib(url):
    '''
    Función que parsea un fichero con pibs de países.
    Parámetros:
        url: Es una cadena con la URL del fichero de texto que contiene el PIB per cápita.
    Devuelve:
        Un diccionario con pares pais:pibs donde pibs es, a su vez, un diccionario con los años y los pibs del país.
    '''
    from urllib import request
    from urllib.error import URLError
    import gzip

    try:
        with request.urlopen(url) as f:
            with gzip.GzipFile(fileobj=f) as gz:
                datos = gz.read().decode('utf-8').split('\n')
    except URLError as e:
        print(f"Error al acceder a la URL: {e}")
        return None

    # Obtenemos los años de la primera línea del fichero.
    if not datos or not datos[0]:
        print("El archivo está vacío o tiene un formato incorrecto.")
        return None

    años = datos.pop(0).split('\t')[1:]
    dict_pibs = {}

    # Procesar las líneas del archivo.
    for pais in datos:
        if not pais.strip():  # Ignorar líneas vacías
            continue
        datos_pais = pais.split('\t')
        if len(datos_pais) < len(años):  # Ignorar datos incompletos
            continue

        codigo_pais = datos_pais.pop(0)[-2:]
        dict_pais = {años[i].strip(): datos_pais[i].strip() for i in range(len(años))}
        dict_pibs[codigo_pais] = dict_pais

    return dict_pibs


def pib(pibs, pais="ES"):
    '''
    Función que recibe un diccionario con los PIBs de los países y muestra por pantalla los PIBs de un país dado.
    Parámetros:
        - pibs: Es un diccionario con los PIBs de los países.
        - pais: Es una cadena con el código del país.
    Salida:
        Muestra por pantalla los PIBs del país indicado.
    '''
    if not pibs or pais not in pibs:
        print(f"El país '{pais}' no se encuentra en los datos.")
        return

    print("Año\tPIB")
    for año, pib in pibs[pais].items():
        print(f"{año}\t{pib}")


# Ejecución del programa
url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"
pibs = parsear_pib(url)
if pibs:
    pais = input("Introduce el código de un país: ")
    print(f"Producto Interior Bruto per cápita de {pais}")
    pib(pibs, pais)