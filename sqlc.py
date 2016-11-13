import csv

import sqlite3


conn = sqlite3.connect('new.db')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE inegi 
                   (renglon INT, año INT, ent TEXT, id_ent INT, 
                    cve_geo INT, sexo TEXT, edad INT, pob INT )  """)


conn.close()

