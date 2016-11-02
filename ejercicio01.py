
import sys
import collections
from urllib.parse import parse_qs
from random import choice
from math import hypot


print(sys.version_info)
print(sys.version)
print("hello", "world", "python 3", "sublime text")

#diferencias entre bytes, str and unicode

# esta fincion recibe str o bytes y siempre regresa str

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)


print(repr(my_values))

print('red ', my_values.get('red'))


creardic = {'animal': ['jirafa'], 'objeto': ['mesa']}
print(creardic)
print(repr(creardic))

Card = collections.namedtuple('Card',['rank','suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards=[Card(rank, suit) for suit in self.suits
                                      for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self,position):
        return self._cards[position]

micarta = Card ('7','diamonds')
print(micarta)
print(len(micarta))
deck = FrenchDeck()
print(len(deck))
print(deck[0])

for i in range (0,51) :
    print (deck[i])

print('ahora:')
print(choice(deck))

lista = [10, 20, 30, 40, 50]
print(lista[:3])
lista = "mi bicicleta es roja"
palabras=lista.split()
print (lista[::-1])
print (deck[12::13])

fruits =['grape', 'rasperry', 'apple', 'banana', 'orange']
print(sorted(fruits,reverse=True))

print (divmod(12, 7))
q, r = divmod(12,7)
print (q)
print (r)

#crea una lista de cuadrados que sean pares
cuadrados = [n*n for n in range(1,11) if not n*n %2]
print (cuadrados)

meses =["ene", "feb", "mar", "abr"]
print (meses*2)


print(hypot(2,2))