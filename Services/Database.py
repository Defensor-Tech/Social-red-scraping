from dotenv import load_dotenv
import os
import pymongo
from pymongo import MongoClient
from http import client

load_dotenv()

Mongoconection = os.getenv('TOKENDATABASE')

client = pymongo.MongoClient(Mongoconection)

db = client['socialmediascrp']
# print(db)

collections_defensor = db['Facebook_json_defensor']
collections_defensor2 = db['Instagram_json_defensor']
# load_dotenv()
# TOKENSOCIAL = os.getenv("TOKENSOCIAL")
# cred = credentials.Certificate(TOKENSOCIAL)
# firebase_admin.initialize_app(cred,{'databaseURL': 'https://scraping-social-red2-default-rtdb.firebaseio.com/'})

def insert_data(data):
    # print(data, "error en la linea 21 de database maldito")
    print("entro a insertar datos")
    collections_defensor.insert_many(data)
    print("datos insertados")
    # print(collections_defensor,"Insertado")

# def insert_data2(data):
#     # print(data, "error en la linea 21 de database maldito")
#     print("entro a insertar datos")
#     collections_defensor2.insert_many(data)
#     print("datos insertados")
#     # print(collections_defensor,"Insertado")

