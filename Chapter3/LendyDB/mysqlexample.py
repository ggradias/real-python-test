import mysql.connector


cnx = mysql.connector(user="root",password="sisteinfo",
                      host='127.0.0.1', database ='videoteca')

print('conexion mysql')

cnx.close()