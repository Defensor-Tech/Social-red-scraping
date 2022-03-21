from datetime import datetime
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
 


def scraping_instagram(keyword,pagina,driver):
    datos = []
    contador = 0

    searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']"))) 
    searchbox.clear() 
    
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
                        print("Scroll Terminado")
                        return
                
                recursiveclick(4)

                elemento = driver.find_elements(By.CLASS_NAME, "C4VMK")
                for element in elemento:   
                    nombre =  element.find_element(By.CLASS_NAME,"_6lAjh ").text
                    comentari = element.find_element(By.CLASS_NAME,"MOdxS ")
                    time.sleep(1)  
                    coment = nombre + ": " + comentari.text
                    cometarios.append(coment)
            except Exception as e:
                print(e)
                
                

            linkk = driver.current_url

            try:
                likes = driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div/div")
                if likes == "Be the first to ":
                    likes = "0"
                else:
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
            fecha = datetime.strptime(fecha, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d')



            rightt = driver.find_elements(By.CLASS_NAME, "l8mY4")
            for left in rightt:
                left.click()
                contador +=1
            if contador == 100:
                break
            dic = dict(titulo=titulo, fuente=fuente,cometarios=cometarios,linkk=linkk,likes=likes,fecha=fecha,pagina=pagina)
            datos.append(dic)
            print(datos)
    
        except Exception as e:
            print(e)
            #print("No hay mas posts")
            break
    print(datos)
    Database.insert_data2(datos)