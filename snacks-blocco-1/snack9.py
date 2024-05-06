#Calcola la somma e la media dei primi 10 numeri.
#Stampa i risultati in console

somma = 0

for i in range(1, 11):
    somma += i

print("La somma è", somma)
print("la media è", somma/10)