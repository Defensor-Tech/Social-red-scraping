from lib2to3.pgen2.driver import Driver
from tkinter import Button 
from turtle import right, title 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.chrome.service import Service
import time 
from Services import Database
 
PATH = "C:/Users/frias/OneDrive - Defensor del Pueblo/Desktop/chromedriver"
s = Service(PATH)

def scraping_instagram():
    datos = []
    url = 'https://www.instagram.com/' 
    
    driver = webdriver.Chrome(service = s) 
    driver.get(url) 
    driver.delete_all_cookies()
    
    username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']"))) 
    password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']"))) 
    
    # username.clear() 
    # username.send_keys("Make_it_exotic") 
    # password.clear() 
    # password.send_keys("Frias123vv") 

    username.clear() 
    username.send_keys("castillopenal0903") 
    password.clear() 
    password.send_keys("Frias123vv") 
    
    button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))) 
    button.click() 
    not_now = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(), "Not Now")]'))).click() 
    not_now2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(), "Not Now")]'))).click() 
    
    searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']"))) 
    searchbox.clear() 
    
    #search for the hashtag cat 
    keyword = "defensorrd" 
    searchbox.send_keys(keyword) 
    
    # Wait for 5 seconds 
    time.sleep(5) 
    searchbox.send_keys(Keys.ENTER) 
    time.sleep(5) 
    searchbox.send_keys(Keys.ENTER) 
    time.sleep(5) 

    time.sleep(4)
    post = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_9AhH0']")))
    post.click()
    while True:
        titulo = None#   
        fuente = 'Instagram'#
        linkk = None# 
        cometarios = []#
        likes = None#
        fecha = None#
        try:
            
            titulo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='_7UhW9   xLCgt      MMzan   KV-D4           se6yk       T0kll ']")))
            time.sleep(1)
            titulo =titulo.text

            try:
                def recursiveclick(invertal):
                    try:
                        contu = driver.find_element(By.XPATH, "//div[@class='             qF0y9          Igw0E     IwRSH        YBx95       _4EzTm                                                                                                            NUiEW  ']")
                        contu.click()
                        time.sleep(invertal)
                        recursiveclick(4)
                    except Exception as e:
                        print(e)
                        print("Scroll Terminado")
                        return
                
                recursiveclick(4)

                elemento = driver.find_elements(By.CLASS_NAME, "C4VMK")
                for element in elemento:     
                    nombre =  element.find_element(By.CLASS_NAME,"_6lAjh ").text
                    comentari = element.find_element(By.CLASS_NAME,"MOdxS ")
                    coment = nombre + ": " + comentari.text
                    cometarios.append(coment)
            except Exception as e:
                print(e)
                
                

            linkk = driver.current_url

            try:
                likes = driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div/div/a/div/span")
                likes = likes.text
            except Exception as e:
                likesclick = driver.find_element(By.CLASS_NAME, "_9Ytll")
                likesclick.click()
                time.sleep(1)
                likes = likesclick.find_element(By.XPATH,"//div[@class='vJRqr']")
                likes = likes.text


            basefecha = driver.find_element(By.CLASS_NAME,'NnvRN ')
            fecha = basefecha.find_element(By.TAG_NAME,'time')
            fecha = fecha.get_attribute('datetime')



            rightt = driver.find_elements(By.CLASS_NAME, "l8mY4")
            for left in rightt:
                left.click()
            dic = dict(titulo=titulo, fuente=fuente,cometarios=cometarios,linkk=linkk,likes=likes,fecha=fecha)
            datos.append(dic)
            Database.insert_data2(datos)
            print(datos)

        except Exception as e:
            print(e)
            #print("No hay mas posts")
            break