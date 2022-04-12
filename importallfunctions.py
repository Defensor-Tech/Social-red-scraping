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
import sched
from RedesSociales.DefensorRd.Scraping_Fabook.pruebafacebok import scraping_faceook as scraping_faceook_defensor
from RedesSociales.DefensorRd.Scraping_Ingram.pruebainsta import scraping_instagram as scraping_instagram_defensor
from dotenv import load_dotenv
import os
