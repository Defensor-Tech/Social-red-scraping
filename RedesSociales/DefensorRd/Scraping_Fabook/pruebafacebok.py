from datetime import date
from email.mime import base
from imghdr import what
from pkgutil import get_data
from typing import Container
from xmlrpc.client import DateTime 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By 
from datetime import datetime
import time 
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os
from Services import Database
from sentiment_analysis_spanish import sentiment_analysis
from sklearn.feature_extraction.text import CountVectorizer
from pysentimiento import create_analyzer
def scraping_faceook(url2,pagina,driver):
    datos = []
    window = driver
    
    def scroll(window):
        
        SCROLL_PAUSE_TIME = 5

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            if len(window.find_elements(By.TAG_NAME, 'article')) >= 100:
                break

            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = window.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            
            print(len(window.find_elements(By.TAG_NAME, 'article')))

        return window.find_elements(By.TAG_NAME, 'article')

  
    #with driver as window:
    window.get(url2) 
    time.sleep(10) 

    container = scroll(driver)
    for element in container: 
        titulo = None   
        fuente = 'facebook' 
        linkk = None 
        comentarios = []
        likes = None
        nombre = None
        fecha = None
        mas = None
        sentiminetcomentario = []
        red = 'facebook'
        time.sleep(2)
        try:
            titulo = element.find_element(By.CLASS_NAME,'_5rgt').text
            # sentiment = sentiment_analysis.SentimentAnalysisSpanish() 
            sentiment = create_analyzer(task="sentiment", lang="es")  
            masclcik = element.find_element(By.CLASS_NAME,'_5rgt').find_element(By.CSS_SELECTOR,"span[data-sigil='more']")
            masclcik.click()
            mas = element.find_element(By.CLASS_NAME,'text_exposed_show')
            titulo = titulo + ' ' + mas.text
            sentimiento = sentiment.predict(titulo).output
        except Exception as e:
            if len(element.find_elements(By.CLASS_NAME,'_5rgt')) <= 206:
                titulo = element.find_element(By.CLASS_NAME,'_5rgt').text
                sentimiento = sentiment.predict(titulo).output
            else:
                titulo = None
                sentimiento = None

        try:
            likes = element.find_element(By.CLASS_NAME,'_1g06').text
        except Exception as e:
            likes = "0"

        try:
            sharedcomenst = element.find_element(By.CLASS_NAME,'_1j-c').text
        except Exception as e:
            sharedcomenst = "0"

        meses = {'enero':'01', 'febrero':'02', 'marzo':'03', 'abril':'04', 'mayo':'05', 'junio':'06', 'julio':'07', 'agosto':'08', 'septiembre':'09', 'octubre':'10', 'noviembre':'11', 'diciembre':'12'}
        def get_month(fehcha: str):

            keys = meses.keys()
            
            for key in keys:
                if fehcha.find(key)!= -1:
                    return meses[key]


        try:
            basefecha = element.find_element(By.CLASS_NAME,'_4g34 ')
            fecha = basefecha.find_element(By.TAG_NAME,'abbr')
            fecha = fecha.text
            if len(fecha) <= 16:
                date = datetime.date(datetime.now())
                fecha = date.strftime('%Y/%m/%d')
            else:
                break
            #     if len(fecha) <= 29:
            #         fecha = fecha[0:2] + "/" + get_month(fecha) + "/" + "2022"
            #     else:
            #         if len(fecha) >= 30:
            #             fecha = fecha[0:2] + "/" + get_month(fecha) + "/" + fecha[-16:-12]
        except Exception as e:
            print(e)
            fecha = None 
    
        try: 
            linkk = element.find_element(By.CLASS_NAME,'_5msj') 
            if linkk: 
                linkk = linkk.get_attribute('href') 
        except Exception as e: 
            print(e) 
            pass 
        try: 
            # Lets open https://www.bing.com/ in the second tab
            window.execute_script("window.open('about:blank','secondtab');")
            window.switch_to.window("secondtab")
            window.get(linkk)
            time.sleep(2)
            try:
                SCROLL_PAUSE_TIME = 2
                last_height = window.execute_script("return document.body.scrollHeight")
                while True:
                    if len(window.find_elements(By.CLASS_NAME,'_108_')) >= 100:
                        break   # If the page is loaded, break the loop
                    # Scroll down to bottom
                    window.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(SCROLL_PAUSE_TIME)
                    try:
                        driver.find_element(By.CLASS_NAME,'_108_').click()
                    except Exception as e:
                        pass
                    # Scroll down to bottom
                    window.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                    # Wait to load page
                    time.sleep(SCROLL_PAUSE_TIME)

                    # Calculate new scroll height and compare with last scroll height
                    new_height = window.execute_script("return document.body.scrollHeight") 
                    if new_height == last_height:

                        elemento = window.find_elements(By.CLASS_NAME,"_2b06")
                        for element in elemento:
                            nombre = element.find_element(By.CLASS_NAME,'_2b05').text
                            comentario = element.find_element(By.CSS_SELECTOR,"div[data-sigil='comment-body']")
                            cometario = nombre + ': ' + comentario.text
                            sentimientocomenta = sentiment.predict(comentario.text).output
                            comentarios.append(cometario)
                            sentiminetcomentario.append(sentimientocomenta)   
                        break
                    last_height = new_height
            
            except Exception as e:
                comentarios = "0"

                print(e)
                time.sleep(2)

            window.close()
            window.switch_to.window(window.window_handles[0])

        except Exception as e: 
            print(e) 
            time.sleep(2)
       

        dic = dict(titulo = titulo, fuente = fuente, link = linkk,likes = likes,sharedorcoments = sharedcomenst,comentarios = comentarios,fecha = fecha,pagina =pagina,sentimiento = sentimiento,sentiminetcomentario = sentiminetcomentario,red = red)
        datos.append(dic) 
        print(datos, "aqui estamos puyando")
    data = Database.insert_data(datos)
    print(data, f"error en pruebafacebook linea 183")



        
