import sqlite3

con = sqlite3.connect("/home/julianne/cloned_git/tpgrp1/tpgr1.db")
cur= con.cursor()
 
for line in cur.execute("SELECT * FROM BITVALUE ;"):
    print(line)


