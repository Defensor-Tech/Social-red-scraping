from selenium import webdriver
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support import expected_conditions as EC
import time
import sched
import os
from selenium.webdriver.chrome.options import Options
import pyrebase
from dotenv import load_dotenv
import requests

load_dotenv()

PATH = os.getenv('W_PATH')

# s = Service(PATH)

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)


def P_Facebook():
    # options = Options()
    # options.add_argument("--headless")

    driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
    driver.get("https://www.facebook.com/")

    print("Iniciando Facebook")

    time.sleep(5)
    email = driver.find_element(By.ID, "email").send_keys("re_chris046@outlook.com")
    time.sleep(5)
    Xpass = driver.find_element(By.ID, 'pass').send_keys("998756725")
    time.sleep(5)

    Lbutton = driver.find_element(By.NAME, 'login')
    # buttonWait = WebDriverWait(driver, 10)
    Lbutton.click()

    time.sleep(15)

    # driver.close()

    print('linea 42',email)
    print(Xpass)
    print(Lbutton)
    time.sleep(15)

    with driver as window:
        window.get("https://m.facebook.com/DefensorRD")

        time.sleep(15)

        container = window.find_elements(By.TAG_NAME,"article") 

        for element in container: 
            titulo = None 
            fuente = 'facebook' 
            link = None
            comentario = None

            time.sleep(8)
 
    
            # titulo = element.text 
            titulo = element.find_element(By.CLASS_NAME,'_5rgt').text

            time.sleep(3)

            try: 
                link = element.find_element(By.CLASS_NAME,'_5msj') 
                if link: 
                    link = link.get_attribute('href') 
            except Exception as e: 
                print(e) 
                pass 

        # try: 
        #     with driver as window: 
        #         window.get(link) 
        #         comentario = window.find_element(By.XPATH,"//div[@data-sigil='comment-body']").text
        # except Exception as e: 
        #     print(e) 
        time.sleep(16) 

        #url = element.find_element(By.TAG_NAME,'a').get_attribute('href') 
        # time.sleep(5) 
 
        dic = dict(titulo = titulo, fuente = fuente, link = link, comentarios = comentario) 
        print(dic)

        # driver.close()

    # driver.close()
    driver.quit()

def Main():
    # s.start()
    # driver = webdriver.Remote(s.service_url, webdriver.DesiredCapabilities.CHROME)
    # driver = webdriver.Chrome(PATH)
    # driver.get("https://www.facebook.com/")
    # driver.close()
    # s.stop()
    P_Facebook()

def IP_CHANGE():

    url = 'https://m.facebook.com/DefensorRD'
    
    #ip address de republica dominicana
    proxies = {
    'http': 'http://181.224.207.18:999',
    'http': 'http://181.36.121.150:999',
    'http': 'http://190.8.47.190:999',
    'http': 'http://181.37.179.49:999',


    }
    response = requests.get(url, proxies=proxies)

    print(response.status_code)
    print(response.json())
    
    # P_Facebook()

P_Facebook()