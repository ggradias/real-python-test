import glob
import os
from numpy import array
from numpy import dot
from numpy import vstack, hstack


my_path = '/suco'

listado = os.walk(my_path)

print (listado)

matrix =  array([[1, 0, 0],[0, 1, 0],[0, 0, 1]])

list = [[1,2,3], [4,5,6], [7,8,9]]

secmatrix = array(list) 

print(matrix*2)
print(matrix[0][1])

print(matrix*secmatrix)
print(dot(secmatrix,matrix))

print(matrix.shape)
print(matrix.diagonal())

