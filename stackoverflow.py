import requests
from bs4 import BeautifulSoup
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}
# URL SEMILLA
url = "https://stackoverflow.com/questions"

# REQUERIMIENTO AL SERVIDOR
respuesta = requests.get(url, headers=headers)

#PARSEO DEL ARBOL CON BEATIFUL SOUP
soup = BeautifulSoup(respuesta.text)
contenedor_de_preguntas = soup.find(id="questions")#ENCONTRAR ELEMENTO POR ID
lista_de_preguntas = contenedor_de_preguntas.find_all('div', class_="question-summary") # ENCONTRAR VARIOS ELEMENTOS POR TAG Y POR CLASE

#for pregunta in lista_de_preguntas: # ITERAR ELEMENTO POR ELEMENTO

    # METODO #1: METODO TRADICIONAL
 #   texto_pregunta = pregunta.find('h3').text # DENTRO DE CADA ELEMENTO ITERADO ENCONTRAR UN TAG
  #  descripcion_pregunta = pregunta.find(class_='excerpt').text  # ENCONTRAR POR CLASE
   # descripcion_pregunta = descripcion_pregunta.replace('\n', '').replace('\r', '') # LIMPIEZA DE TEXTO
    #print(texto_pregunta)
    #print(descripcion_pregunta)

    #print()

for pregunta in lista_de_preguntas: # ITERAR ELEMENTO POR ELEMENTO
    elemento_texto_pregunta = pregunta.find('h3')
    texto_pregunta = elemento_texto_pregunta.text

    descripcion_pregunta = elemento_texto_pregunta.find_next_sibling('div').text

    descripcion_pregunta = descripcion_pregunta.replace('\n', '').replace('\r', '')  # LIMPIEZA DE TEXTO
    print(texto_pregunta)
    print(descripcion_pregunta)

    print()








    
 
 












