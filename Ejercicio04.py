#Escribir un programa que acceda al fichero de internet mediante la url
#indicada y muestre por pantalla el número de palabras que contiene.
def contar_palabras(url):

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

