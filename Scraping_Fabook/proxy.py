import requests
import json

#PATH = "C:/Users/frias/OneDrive - Defensor del Pueblo/Desktop/chromedriver"
# def get_proxy_arr():

#     url = "https://proxy.webshare.io/proxy/list/download/yvcecddpomcmhyfobwgymcjgfrzhuqeblyinjrvu/NL/http/port/direct/"

#     r = requests.get(url)
#     p_arr=[{

#          "proxy": item.split("\\")[0].replace("b'","")

#         } for item in str(r.content).split('r\\n')[:-1]]

#     return p_arr


def get_proxy_arr():

    url = 'http://list.didsoft.com/get?email=datawharehousedp@gmail.com&pass=jd864c&pid=socks4100&showcountry=yes&showversion=yes&version=socks5'

    #response = requests.post(url, proxies=proxies)
    response = requests.get(url)
    p_arr = [{
            "proxy" : item.split("#")[0],
            "socks":  item.split("#")[1],
            "country": item.split("#")[2],
            


        } for item in str(response.content).split('\\n')[:-1]]

    return p_arr

get_proxy_arr()





    
