#Escribir un programa que acceda al fichero de internet mediante la url
#indicada y muestre por pantalla el número de palabras que contiene.
import urllib.request


def read_url(url):
    archivo = urllib.request.urlopen(url)
    for line in archivo:
        linea= line.decode("utf-8")
        print(linea)
    return


url = 'http://textfiles.com/adventure/aencounter.txt'
read_url(url)

