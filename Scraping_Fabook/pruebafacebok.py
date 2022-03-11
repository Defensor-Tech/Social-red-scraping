from imghdr import what
from typing import Container 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By 
import time 
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os
#from proxy import get_proxy_arr

#proxy_list = get_proxy_arr()
# load_dotenv()
# PATH = os.getenv('W_PATH')

def scraping_faceook():
    PATH = "C:/Users/frias/OneDrive - Defensor del Pueblo/Desktop/chromedriver"
    s = Service(PATH)
    #caps = webdriver.DesiredCapabilities.CHROME.copy() 
    options = webdriver.ChromeOptions()
    #ignora los certificados de seguridad y certificado
    options.add_argument('--ignore-certificate-error')

    #ignora los certificados que sean erroneos
    options.add_argument('--ignore-certificate-errors-spki-list')

    #desactiva los errores que pueda dar  el ssl
    options.add_argument('--ignore-ssl-errors')

    #options.add_argument('--user-agent=%s' % ua)
    #caps['acceptInsecureCerts'] = True
    url = 'https://facebook.com/'

    # for eachProxy in proxy_list[1:]:

    def scroll(driver):
        SCROLL_PAUSE_TIME = 5

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            if len(window.find_elements(By.TAG_NAME, 'article')) >= 10:
                break
                
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            
            print(len(window.find_elements(By.TAG_NAME, 'article')))
        
        return window.find_elements(By.TAG_NAME, 'article')

    try:
        PROXY = "154.16.89.172:45785"
        #options.add_argument('--proxy-server=%s' % PROXY)
        driver = webdriver.Chrome(service = s,options=options)
        driver.get(url)
        time.sleep(10)
    except:
        print("hello")


    username =driver.find_element(By.ID, 'email') 
    password = driver.find_element(By.ID, 'pass')    
    username.send_keys('jc7645085@gmail.com') 
    password.send_keys('Frias123vv') 
    enter = driver.find_element(By.NAME,'login') 
    time.sleep(5)
    enter.click() 
    time.sleep(10) 
    with driver as window:  
        window.get("https://m.facebook.com/LuisAbinaderCorona") 
        time.sleep(10) 

        
        container = scroll(driver)
        for element in container: 
            titulo = None   
            fuente = 'facebook' 
            linkk = None 
            cometarios = [] 
            likes = None
            nombre = None
            shared = None

            time.sleep(2)
            titulo = element.find_element(By.CLASS_NAME,'_5rgt').text 
            try:
                likes = element.find_element(By.CLASS_NAME,'_1g06').text
            except Exception as e:
                likes = None

            try:
                sharedcomenst = element.find_element(By.CLASS_NAME,'_1j-c').text
            except Exception as e:
                sharedcomenst = None
        
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
                            break
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
                                cometarios.append(cometario)
                            break
                        last_height = new_height
                
                except Exception as e:
                    print(e)
                    time.sleep(2)

                window.close()
                window.switch_to.window(window.window_handles[0])
            except Exception as e: 
                print(e) 
                time.sleep(2)

            dic = dict(titulo = titulo, fuente = fuente, link = linkk,likes = likes,sharedorcoments = sharedcomenst,comentarios = cometarios) 
            print(dic)



        
