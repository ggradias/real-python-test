import sqlite3

with sqlite3.connect("new.db") as cnx:
    c = cnx.cursor()

    c.execute(""" SELECT DISTINCT population.city, population.population, regiones.region FROM population, regiones 
                  WHERE population.city = regiones.city ORDER by population.city ASC""")

    rows = c.fetchall()

    for r in rows:
        print("city:"+r[0]+"\n")
        print("population:"+str(r[1])+"\n")
        print("region:"+r[2])


    c.close()

