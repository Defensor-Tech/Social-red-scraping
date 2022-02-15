from typing import Container 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By 
import time 
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os

load_dotenv()

PATH = os.getenv('W_PATH')

s = Service(PATH)

opt = webdriver.ChromeOptions()

#ignora los certificados de seguridad y certificado
opt.add_argument('--ignore-certificate-error')

#ignora los certificados que sean erroneos
opt.add_argument('--ignore-certificate-errors-spki-list')

#desactiva los errores que pueda dar  el ssl
opt.add_argument('--ignore-ssl-errors')

#DesiredCapabilities

caps = webdriver.DesiredCapabilities.CHROME.copy() 

caps['acceptInsecureCerts'] = True

 
# PATH = "C:/Users/frias/OneDrive - Defensor del Pueblo/Desktop/chromedriver"
url = 'https://www.facebook.com/' 
 
driver = webdriver.Chrome(service = s, options=opt, desired_capabilities=caps) 
driver.get(url) 
 
username =driver.find_element(By.ID, 'email') 
password = driver.find_element(By.ID, 'pass')    
username.send_keys('jc7645085@gmail.com') 
password.send_keys('Frias123vv') 
enter = driver.find_element(By.NAME,'login') 
enter.click() 
time.sleep(10) 
with driver as window:  
    window.get("https://m.facebook.com/DefensorRD") 
    time.sleep(2) 
 
    container = window.find_elements(By.TAG_NAME,"article") 
    for element in container: 
        titulo = None 
        fuente = 'facebook' 
        linkk = None 
        cometarios = None 
        megusta = None
        coment = None
        shared = None

        titulo = element.find_element(By.CLASS_NAME,'_2pim').text 
        megusta = element.find_element(By.CLASS_NAME,'_1g06').text
        sharedcomenst = element.find_element(By.CLASS_NAME,'_1j-c').text
    
        try: 
            linkk = element.find_element(By.CLASS_NAME,'_5msj') 
            if linkk: 
                linkk = linkk.get_attribute('href') 
        except Exception as e: 
            print(e) 
            pass 
        try: 
            with window as window: 
                window.get(linkk) 

                time.sleep(5)

                contenedor = window.find_element(By.XPATH,"//div[@class='_6j_d show']")

                print(contenedor.text)

                atras = contenedor.find_element(By.CLASS_NAME,"_6j_c")

                # atras_2 = window.find_element_by_css_selector(".reply-button").click()

                print(atras.text)

                cometarios = window.find_element(By.CLASS_NAME,"_2b06").text
                #shared = window.find_element(By.XPATH,"//div[@data-sigil='share-count']").text

                atras.click()

                time.sleep(10)

        except Exception as e: 
            print(e) 
            time.sleep(16)
 
        dic = dict(titulo = titulo, fuente = fuente, link = linkk,likes = megusta,sharedorcoments = sharedcomenst,comentarios = cometarios) 
        print(dic)