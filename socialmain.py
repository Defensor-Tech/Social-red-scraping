from importallfunctions import *

#-------------------------------Actualizador automatico---------------------------------------
timeout = 0 # Segundos
s = sched.scheduler(time.time, time.sleep)

def do_something(sc):
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
    # for eachProxy in proxy_list[1:]:
    url = 'https://facebook.com/'
    # #PROXY = "154.16.89.172:45785"
    #options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(service = s,options=options)
    driver.get(url)
    time.sleep(10)
   
    username =driver.find_element(By.ID, 'email') 
    password = driver.find_element(By.ID, 'pass') 
    username.send_keys('jc7645085@gmail.com') 
    password.send_keys('Frias123vv') 
    enter = driver.find_element(By.NAME,'login') 
    time.sleep(5)
    enter.click() 
    time.sleep(10)


    scraping_faceook_defensor("https://m.facebook.com/DefensorRd/", "DefensorRd",driver)
    scraping_faceook_defensor("https://m.facebook.com/acento.com.do/" , "Acento",driver)
    scraping_faceook_defensor("https://m.facebook.com/ANoticias7/", "ANoticias7",driver)
    scraping_faceook_defensor("https://m.facebook.com/cachicha/?__nodl&_rdr/", "Cachicha",driver)
    scraping_faceook_defensor("https://m.facebook.com/colorvisionc9/", "Colorvision",driver)
    scraping_faceook_defensor("https://m.facebook.com/DiarioLibre/", "DiarioLibre",driver)
    scraping_faceook_defensor("https://m.facebook.com/ElCaribe.com.do/", "ElCaribe",driver)
    scraping_faceook_defensor("https://m.facebook.com/elnuevodiariord/", "ElNuevoDiario",driver)
    scraping_faceook_defensor("https://m.facebook.com/lascalientesdelsur.net/", "Lascalientes",driver)
    scraping_faceook_defensor("https://m.facebook.com/listindiario/", "ListinDiario",driver)
    scraping_faceook_defensor("https://m.facebook.com/loultimodigital?tsid=0.5338720946387234&source=result", "LoultimoDigital",driver)
    scraping_faceook_defensor("https://m.facebook.com/LuisAbinaderCorona", "LuisAbinader",driver)
    scraping_faceook_defensor("https://m.facebook.com/Minuto-A-Minuto-1287877911298818/?ref=content_filter&__nodl&_rdr", "minutoaminuto",driver)
    scraping_faceook_defensor("https://m.facebook.com/SIN24Horas/", "SIN24Horas",driver)
    scraping_faceook_defensor("https://m.facebook.com/nuriapiera/", "Nuriapiera",driver)
    scraping_faceook_defensor("https://m.facebook.com/puertoplatadigital/", "puertoplatadigital",driver)
    scraping_faceook_defensor("https://m.facebook.com/remolacha.net/", "Remolacha",driver)
    scraping_faceook_defensor("https://m.facebook.com/telesistema/", "telesistema",driver)
    scraping_faceook_defensor("https://m.facebook.com/z101digital/", "Z101Digital",driver)


    # urlins = 'https://www.instagram.com/'
    
    # driver.get(urlins) 
    # driver.delete_all_cookies()
    
    # username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']"))) 
    # password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']"))) 
    
    # try:
    #     username.clear() 
    #     username.send_keys("castillopenal0903") 
    #     password.clear() 
    #     password.send_keys("Frias123vv")  
    # except Exception as e:
    #     username.clear() 
    #     username.send_keys("Make_it_exotic") 
    #     password.clear() 
    #     password.send_keys("Frias123vv") 
        
    
    # button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))) 
    # button.click() 
    # not_now = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(), "Not Now")]'))).click() 
    # not_now2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(), "Not Now")]'))).click() 
    

    # scraping_instagram_defensor("defensorrd", "DefensorRd",driver)
    # scraping_instagram_defensor("acentodiario", "Acento",driver)
    # scraping_instagram_defensor("anoticias7", "ANoticias7",driver)
    # scraping_instagram_defensor("cachicha.sd", "Cachicha",driver)
    # scraping_instagram_defensor("colorvisionc9", "Colorvision",driver)
    # scraping_instagram_defensor("diariolibre", "DiarioLibre",driver)
    # scraping_instagram_defensor("elcariberd", "ElCaribe",driver)
    # scraping_instagram_defensor("elnuevodiariord", "ElNuevoDiario",driver)
    # scraping_instagram_defensor("calientesdelsur", "Lascalientes",driver)
    # scraping_instagram_defensor("listindiario", "ListinDiario",driver)
    # scraping_instagram_defensor("loultimodigital", "LoultimoDigital",driver)
    # scraping_instagram_defensor("luisabinader", "LuisAbinader",driver)
    # scraping_instagram_defensor("rcavada", "robertoCabada",driver)
    # scraping_instagram_defensor("sin24horas", "SIN24Horas",driver)
    # scraping_instagram_defensor("nuriapiera", "Nuriapiera",driver)
    # scraping_instagram_defensor("puertoplatadigital", "puertoplatadigital",driver)
    # scraping_instagram_defensor("remolachanet", "Remolacha",driver)
    # scraping_instagram_defensor("telesistema11rd", "telesistema",driver)
    # scraping_instagram_defensor("z_digital", "Z101Digital",driver)



    timeout = 3600
    s.enter(timeout, 1, do_something, (sc,))


s.enter(timeout, 1, do_something, (s,))
s.run()



print("------------------------------------------SE ACTUALIZA---------------------------------------------------------------------")
