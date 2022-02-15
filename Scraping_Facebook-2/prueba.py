from typing import Container
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from proxy import get_proxy_arr


proxy_list = get_proxy_arr()

for eachProxy in proxy_list[1:]:

    PATH = "C:/Users/frias/OneDrive - Defensor del Pueblo/Desktop/chromedriver"
    url = 'https://whoer.net/'


    try:
        options = Options()
        options.add_argument('--proxy-server=%s' % eachProxy['proxy'])
        driver = webdriver.Chrome(PATH,options=options)
        driver.get(url)
        time.sleep(10)
    except:
        print(eachProxy["proxy"] + " is not working")

# print("Done")
# username =driver.find_element(By.ID, 'email')
# password = driver.find_element(By.ID, 'pass')   
# username.send_keys('jc7645085@gmail.com')
# password.send_keys('Frias123vv')
# enter = driver.find_element(By.NAME,'login')
# enter.click()
# time.sleep(10)
# with driver as window: 
#     window.get("https://m.facebook.com/DefensorRD")
#     time.sleep(10)

#     container = window.find_elements(By.TAG_NAME,"article")
#     for element in container:
#         titulo = None
#         fuente = 'facebook'
#         linkk = None
#         cometarios = None

#         titulo = element.find_element(By.CLASS_NAME,'_5rgt').text
#         try:
#             linkk = element.find_element(By.CLASS_NAME,'_5msj')
#             if linkk:
#                 linkk = linkk.get_attribute('href')
#         except Exception as e:
#             print(e)
#             pass
#             time.sleep(16)

#         dic = dict(titulo = titulo, fuente = fuente, link = linkk,comentarios = cometarios)
#         print(dic)