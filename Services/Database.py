import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
from dotenv import load_dotenv
import os

load_dotenv()
TOKENSOCIAL = os.getenv("TOKENSOCIAL")
cred = credentials.Certificate(TOKENSOCIAL)
firebase_admin.initialize_app(cred,{'databaseURL': 'https://scraping-social-red2-default-rtdb.firebaseio.com/'})

def insert_data(data):
    ref= db.reference('/')
    users_ref = ref.child('RedSocial').child('Facebook')
    users_ref.set(data)
    print(users_ref,"Insertado")

def insert_data2(data):
    ref= db.reference('/')
    users_ref = ref.child('RedSocial').child('Instagram')
    users_ref.set(data)
    print(users_ref,"Insertado")