from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E

URL = "https://www.diariooficial.interior.gob.cl/edicionelectronica/marcas_patentes.php?date=19-06-2020&edition=42685"

#######  Algoritmo descarga múltiple  PDF´S MARCAS Diario Oficial Chile ############################

wait_time_out = 15
driver = webdriver.Chrome('./chromedriver')
driver.get(URL)
wait_variable = W(driver, wait_time_out)
links = wait_variable.until(E.visibility_of_all_elements_located((By.TAG_NAME, "a")))
print("Numero de links", len(links))
for link in links:
    print(link.text)



