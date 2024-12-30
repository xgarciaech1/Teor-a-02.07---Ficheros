#Escribir un programa que acceda al fichero de internet mediante la url
#indicada y muestre por pantalla el número de palabras que contiene.
'''import urllib.request


def read_url(url):
    archivo = urllib.request.urlopen(url)
    for line in archivo:
        linea= line.decode("utf-8")
        print(linea)
    return


url = 'http://textfiles.com/adventure/aencounter.txt'
read_url(url)
'''

def contar_palabras(url):
    '''
    Función que recibe recibe la url de un fichero de texto y devuelve el número de palabras que contiene.
    Parámetros:
        url: Es una cadena con la url del fichero de texto.
    Devuelve:
        El número de palabras que contiene el fichero de texto daro por la url.
    '''
    from urllib import request
    from urllib.error import URLError
    try:
        f = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        contenido = f.read()
        return len(contenido.split())

print(contar_palabras('hhttp://textfiles.com/adventure/aencounter.txt'))
print(contar_palabras('https://no-existe.txt'))
