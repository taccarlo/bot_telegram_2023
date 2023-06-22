
# avere cura di lanciare lo script python dalla stessa cartella in cui è presente il .db, 
# che se no creerà due database vuoti e quindi si 
# lamenterà che i db creati non hanno le table adeguate.

import sqlite3
db = sqlite3.connect("./weather.db")
print("Opened database successfully");


try:
    cursor = db.cursor()
    query = "SELECT Data, Ora,Wind  from  dump_dati_stazioni_VR where wind > 300"
    cursor.execute(query)
    stazCoords = cursor.fetchall()
    print(stazCoords)
except sqlite3.Error as sqlerror:
    print("Error while connecting to sqlite", sqlerror)
