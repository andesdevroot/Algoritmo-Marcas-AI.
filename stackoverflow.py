import requests
from bs4 import BeautifulSoup
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}
# URL SEMILLA
url = "https://stackoverflow.com/questions"

# REQUERIMIENTO AL SERVIDOR
respuesta = requests.get(url, headers=headers)

#PARSEO DEL ARBOL CON
soup = BeautifulSoup(respuesta.text)

contenedor_de_preguntas = soup.find(id="questions")
lista_de_preguntas = contenedor_de_preguntas.find_all('div', class_="question-sumary")

for pregunta in lista_de_preguntas:
    texto_pregunta = pregunta.find('h3').text
    print(texto_pregunta)









