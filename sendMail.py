import sqlite3
import mysql.connector 
import pandas as pd
import subprocess

con = sqlite3.connect("tpgr1.db")
cur= con.cursor()
df = pd.read_sql_query("SELECT * FROM bitvalue ;", con)



# # for line in cur.execute("SELECT * FROM bitvalue ;"):
# #     print(line)

count=0


for i in range(len(df)-1):
    if df.iloc[i,1] < df.iloc[i+1,1]:
        count+=1
        if count==-5:
            subprocess.run(["python3 mailUp.py"])

    if df.iloc[i,1] > df.iloc[i+1,1]:
        count-=1
        if count==5:
            subprocess.run(["python3 mailDown.py"])   
