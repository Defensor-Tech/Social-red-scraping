import requests
import json

#PATH = "C:/Users/frias/OneDrive - Defensor del Pueblo/Desktop/chromedriver"
def get_proxy_arr():

    url = "https://proxy.webshare.io/proxy/list/download/yvcecddpomcmhyfobwgymcjgfrzhuqeblyinjrvu/US/http/port/direct/"

    r = requests.get(url)

    p_arr=[{

         "proxy": item.split("\\")[0].replace("b'","")

        } for item in str(r.content).split('r\\n')[:-1]]

    return p_arr


get_proxy_arr()
