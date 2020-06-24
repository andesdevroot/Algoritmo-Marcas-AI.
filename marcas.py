import requests
from lxml import html


encabezados = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}

### URL ESTATICA
url = "https://www.diariooficial.interior.gob.cl/edicionelectronica/marcas_patentes.php?date=12-06-2020&edition=42679"

respuesta = requests.get(url, headers=encabezados)

#parsear los datos del arbol html

parser = html.fromstring(respuesta.text)

#ingles = parser.get_element_by_id("js-link-box-en")
#print (ingles.text_content())

#ingles = parser.xpath("//a[@id='js-link-box-en']/strong/text()")
#print(ingles)


#ingles = parser.xpath("//a[@id='js-link-box-en']/strong/text()")
#print(ingles)

#idiomas = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()")

 #for idioma in idiomas:
  # print(idiomas)

# PARSEO DE CLASE PADRE ARBOL HTML###########
idiomas = parser.find_class('content')

# IMPRESION EN CONSOLA PYTHON DE SCRAPING ########
for idioma in idiomas:
 print(idioma.text_content())

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    














