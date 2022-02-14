from typing import Container 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By 
import time 
 
PATH = "C:/Users/frias/OneDrive - Defensor del Pueblo/Desktop/chromedriver"
url = 'https://www.facebook.com/' 
 
driver = webdriver.Chrome(PATH) 
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
    time.sleep(10) 
 
    container = window.find_elements(By.TAG_NAME,"article") 
    for element in container: 
        titulo = None 
        fuente = 'facebook' 
        linkk = None 
        cometarios = None 
        megusta = None
        coment = None
        shared = None

        titulo = element.find_element(By.CLASS_NAME,'_5rgt').text 
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
                cometarios = window.find_element(By.CLASS_NAME,"_2b06").text
                #shared = window.find_element(By.XPATH,"//div[@data-sigil='share-count']").text
        except Exception as e: 
            print(e) 
            time.sleep(16)
 
        dic = dict(titulo = titulo, fuente = fuente, link = linkk,likes = megusta,sharedorcoments = sharedcomenst,comentarios = cometarios) 
        print(dic)