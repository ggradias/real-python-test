from random import randint



heads = 0
tails = 0


for trial in range(0,10000):
    while randint(0,1)==0:
        tails = tails + 1
    heads = heads + 1



print ("heads/tails =", heads,tails,heads/(heads+tails))

resultado = 0
for dice in range(0,10000):
    resultado = resultado + randint(1,6)

print (dice+1, ' la respuesta es ', resultado/(dice+1))