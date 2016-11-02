from random import random,randint


'''

Se utiliza el método de Montecarlo
   REGION 1

   0      .13       0      .13
   1      .87       0.13   1

   REGION 2

   0      .35       0      .35
   1      .65       0.35   1

   REGION 3

   0      .83       0      .83
   1      .17       0.83    1


'''
region1a=0
region1b=0
region2a=0
region2b=0
region3a=0
region3b=0


suma = 0

for i in range(1,10000+1):
    region = randint(1,3)
    num=random()
    if region ==1:
        if num > 0.13:
            region1a=region1a+1
        else:
            region1b=region1b+1
    elif region ==2:
        if num > 0.35:
            region2a=region2a+1
        else:
            region2b=region2b+1
    else:
        if num > 0.83:
            region3a=region3a+1
        else:
            region3b=region3b+1

 # and the winner is ...
a= 0
b=0
if region1a > region1b:
    a = a+1
else:
    b = b +1
if region2a > region2b:
    a = a+1
else: 
    b = b+1
if region3a > region3b:
    a = a +1
else:
    b = b +1





print('1-a ',region1a)
print('1-b ',region1b)
print('2-a ',region2a)
print('2-b ',region2b)
print('3-a ',region3a)
print('3-b ',region3b)
region1 = region1a+region1b
region2 = region2a + region2b
region3 = region3a + region3b


print('total ',region1+region2+region3)
if a > b :
    print ('ganó A en {} regiones de 3'.format(a))
else:
    print ('gano B en {} regiones de 3'.format(a))