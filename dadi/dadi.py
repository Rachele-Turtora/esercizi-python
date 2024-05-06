#Generare un numero random da 1 a 6, sia per il giocatore sia per il computer.
#Stabilire il vincitore, in base a chi fa il punteggio più alto.

import random

user_number = random.randrange(1, 7)
print("Il tuo numero è:", user_number)

computer_number = random.randrange(1, 7)
print("Il numero del computer è:", computer_number)

if user_number > computer_number:
    print("Hai vinto")
elif computer_number > user_number:
    print("Ha vinto il computer")
else:
    print("Parità")