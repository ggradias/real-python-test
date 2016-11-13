import sqlite3

with sqlite3.connect("new.db") as cnx:
    c = cnx.cursor()
    c.execute("INSERT INTO population VALUES ('New York City','NY',8200000)")
    c.execute("INSERT INTO population VALUES ('San Francisco','CA',8000000)")
    c.close()


