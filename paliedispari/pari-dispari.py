#L’utente sceglie pari o dispari e inserisce un numero da 1 a 5.
#Generiamo un numero random (sempre da 1 a 5) per il computer.
#Sommiamo i due numeri
#Stabiliamo se la somma dei due numeri è pari o dispari (usando una funzione)
#Dichiariamo chi ha vinto.

import random

user_choice = ""
while user_choice != "pari" and user_choice != "dispari":
    user_choice = input("Scegli pari o dispari: ").lower()

user_num = ""
while not user_num.isdigit() or int(user_num) < 1 or int(user_num) > 6:
    user_num = input("Scegli un numero da 1 a 5: ")

computer_num = random.randrange(1, 6)

sum = int(user_num) + int(computer_num)

def even_odd(num):
    if num % 2 == 0: return "pari"
    return "dispari"

print("Hai scelto", user_choice)
print("Il tuo numero è", user_num)
print("Il numero del computer è", computer_num)
print("La somma è:", sum)

if even_odd(sum) == user_choice:
    print("Hai vinto")
else:
    print("Il computer ha vinto")
