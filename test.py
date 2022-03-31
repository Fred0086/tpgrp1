import sqlite3

con = sqlite3.connect("tpgr1.db")
cur= con.cursor()
 
for line in cur.execute("SELECT * FROM bitvalue ;"):
    print(line)


