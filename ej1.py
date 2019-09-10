#Autor Elias Daniel Cobo Medvedsky#

import re
from collections import Counter
from newspaper import Article

def body(url):
    '''Funcion que dado una url de un articulo, lo parsea con una determinada expresion regular y retonra un diccionario ordenado por valor de la cantidad de ocurrencias de palabras'''
    article = Article(url)
    article.download()
    article.parse()
    text = article.text.lower()
    counter = Counter(filter(None,re.split(r'[\W\d]+', text)))
    return dict(sorted(counter.items(), key=lambda kv: kv[1], reverse=True))
    