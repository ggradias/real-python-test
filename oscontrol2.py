import os
import time
import glob
import shutil as sh



# se obtiene un listado del contenido del directorio actual
directorio = os.listdir('.')
print(directorio)

# se obtiene la funcion estadistica para obtener informacion acerca 
# de archivo



estadistica = os.stat('bits.py')
print(estadistica)


# se obtiene informacion acerca del tiempo local
# basicamente convietrte un valor entero 
# a un formato de fecha de forma estructurada

tiempo = time.localtime(1474250903)
print(tiempo)
# aqui propieamente en el formato fechas
print(time.strftime("%Y-%m-%d", tiempo))

# esta codificada en nueve bits, similar al bitmask pero se lee al reves
#en grupos de tres
print(bin(estadistica.st_mode)[-9:])

# muestra el directorio actual
cwd = os.getcwd()
print(cwd)

# muestra el contenido del directorio actual
contenido = os.listdir(cwd)
print(contenido)

# crea un subdirectorio
# os.mkdir('subdir')


# nos cambiamos al subdirectorio

#os.chdir('subdir')

print(os.getcwd())

listaglob = glob.glob('*') # se pueden usar comodines *.??

print (listaglob)
 

ahora = time.time()
print(ahora)

gmt = time.gmtime(ahora)
