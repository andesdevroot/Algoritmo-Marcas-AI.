import requests
filename = "marca.pdf"
document_url = "https://www.diariooficial.interior.gob.cl/publicaciones/2020/06/12/42679/06/1771745.pdf"
with open(filename, 'wb') as f:
    f.write(requests.get(document_url).content)
