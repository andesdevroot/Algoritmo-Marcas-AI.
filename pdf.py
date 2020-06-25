from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

# Download Archivo txt

driver.find_element_by_id("textbox").send_keys("probando bajada de pdf")
driver.find_element_by_id("createTxt").click() # HACE CLICK EN EL BOTON BAJADA DE PDF
driver.find_element_by_id("link-to-download").click() # Link para bajar el archivo

# Download Archivo Pdf

driver.find_element_by_id("pdfbox").send_keys("testing.pdf")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()

#driver.close()


