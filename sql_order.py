import sqlite3


with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE regiones (city TEXT, region TEXT)""")

    cities = [
               ('New York City', 'Northeast'),
               ('San Francisco', 'West'),
               ('Chicago', 'Midwest'),
               ('Houston', 'South'),
               ('Phoenix', 'West'),
               ('Boston', 'Northeast'),
               ('Los Angeles', 'West'),
               ('Philadelphia', 'Northeast'),
               ('San Antonio', 'South'),
               ('San Diego', 'West'),
               ('Dallas', 'South'),
               ('San Jose', 'West'),
               ('Jacksonville', 'South'),
               ('Indianapolis', 'Midwest'),
               ('Austin', 'South'),
               ('Detroit', 'Midwest') ]

    c.executemany("INSERT INTO regiones VALUES(?, ?)", cities)
    c.execute("SELECT * FROM regiones ORDER BY region ASC")

    rows = c.fetchall()

    for r in rows:
      print(r[0], r[1])  
    c.close()