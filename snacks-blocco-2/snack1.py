#Crea due array che hanno un numero di elementi diversi.
#Aggiungi elementi casuali all’array che ha meno elementi,
#fino a quando ne avrà tanti quanti l’altro.

import random

lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2]

if len(lista1) < len(lista2):
    min_list = lista1
elif len(lista2) < len(lista1):
    min_list = lista2
else:
    print("La lunghezza è uguale")

while len(lista1) != len(lista2):
    min_list.append(random.randrange(1, 11))

print(lista1, len(lista1))
print(lista2, len(lista2))