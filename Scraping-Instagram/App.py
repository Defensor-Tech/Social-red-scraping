from tkinter import Button 
from turtle import title 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait 
import time 
 
PATH = "C:/Users/frias/Downloads/chromedriver_win32 (1)/chromedriver" 
url = 'https://www.instagram.com/' 
 
driver = webdriver.Chrome(PATH) 
driver.get(url) 
 
username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']"))) 
password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']"))) 
 
username.clear() 
username.send_keys("Make_it_exotic") 
password.clear() 
password.send_keys("Frias123vv") 
 
button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))) 
button.click() 
not_now = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(), "Not Now")]'))).click() 
#not_now2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(), "Not Now")]'))).click() 
 
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
 
driver.execute_script("window.scrollTo(0,4000);") 
 
post = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="v1Nh3 kIKUG  _bz0w"]'))) 
post.click() 
titulo = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="C4VMK"]'))) 
print(titulo.text) 
 
 
 
# titulo1 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="C4VMK"]'))) 
# for titulos in titulo1: 
#     print(titulos.text)