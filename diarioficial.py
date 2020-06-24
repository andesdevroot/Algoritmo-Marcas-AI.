import requests
from bs4 import BeautifulSoup
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}

#URL SEMILLA DIARIO OFICIAl 12

url = "https://www.diariooficial.interior.gob.cl/edicionelectronica/marcas_patentes.php?date=12-06-2020&edition=42679"

#REQUERIMIENTO DEL SERVIDOR

respuesta = requests.get(url, headers=headers)

#PARSEO DEL ARBOL CON BEATIFUL SOUP
soup = BeautifulSoup(respuesta.text)
contenedor_de_preguntas = soup.find(id="#")#ENCONTRAR ELEMENTO POR ID
lista_de_preguntas = contenedor_de_preguntas.find_all('td', class_="content") # ENCONTRAR VARIOS ELEMENTOS POR TAG Y POR CLASE


for pregunta in lista_de_preguntas: # ITERAR ELEMENTO POR ELEMENTO
    elemento_texto_pregunta = pregunta.find('content')
    texto_pregunta = elemento_texto_pregunta.text

    descripcion_pregunta = elemento_texto_pregunta.find_next_sibling('td').text


    print(texto_pregunta)
    print(descripcion_pregunta)

    print()


