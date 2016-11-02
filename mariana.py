import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root', password='sisteinfo', host='127.0.0.1', database='videoteca')
cursor = cnx.cursor()

query = ("SELECT * FROM pelicula ")



cursor.execute(query)

for (titulo, director, interprete) in cursor:
  print("{}, {} was {} ".format(
    titulo, director, interprete))

cursor.close()
cnx.close()
