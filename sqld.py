import csv
import sys
import sqlite3


with sqlite3.connect("new.db") as cnx:
    
    c = cnx.cursor()
    poblacionmx = csv.reader(open('poblacion.csv', "rU"))

    c.executemany("INSERT INTO inegi (renglon, ano, ent, id_ent, cve_geo, sexo, edad, pob)  values(?,?,?,?,?,?,?,?)", poblacionmx)

    c.close()