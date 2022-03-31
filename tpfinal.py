import sqlite3
from datetime import datetime
from sqlite3 import Timestamp
import requests
import time
import json
import hmac
import hashlib
from urllib.parse import urljoin, urlencode

params = None

# Création d'une boucle pour récupérer valeur du bitcoin + la date 
# les requêtes sont effectuées chaque minute

while 1==1 :
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCEUR"
    reponse = requests.get(url)
    data2=reponse.json()
    print(reponse.json())

    for cle, valeur in data2.items():
        price=valeur

    urlt=urljoin('https://api.binance.com','/api/v1/time')
    r = requests.get(urlt, params=params)

    print(r.json())
    data=r.json()
    for cle, valeur in data.items():
        timestamp=valeur
        
    dt_object = datetime.fromtimestamp(timestamp/1000)
    print(dt_object)
    


    # sqlite

    con = sqlite3.connect('tpgr1.db')   #créa en local 
    cur = con.cursor()
    now=datetime.now()
    

    ###### To Recerate table if needed : 
    #           cur.execute("Create table IF NOT EXISTS bitvalue (id int, valeur float,date timestamp);")


    cur.execute("INSERT INTO bitvalue (valeur,date) VALUES ("+str(price)+","+str(timestamp/1000)+");")
    con.commit()
    con.close()
    time.sleep(60)


