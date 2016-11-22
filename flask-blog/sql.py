import sqlite3

with sqlite3.connect("blog.db") as cnx:
   c = cnx.cursor()
   c.execute("""CREATE TABLE posts
            (title text, contenido text) """)
   c.execute("""INSERT INTO posts VALUES ('GOOD','Im good')""")
   c.execute("""INSERT INTO posts VALUES ('WELL','Im well')""")
   c.execute("""INSERT INTO posts VALUES ('EXCELENT','Im excellent')""")
   c.execute("""INSERT INTO posts VALUES ('OKAY','Im OK')""") 
   c.close()
  