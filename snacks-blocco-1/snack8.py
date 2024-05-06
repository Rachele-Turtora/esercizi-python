#Chiedi un numero di 4 cifre all’utente
#Calcola la somma di tutte le cifre che compongono il numero.
#Stampa il risultato in console

somma = 0

while True:
    try:
        num = input("Inserisci un numero di 4 cifre: ")
        if type(int(num)) == int and len(num) == 4:
            for n in num:
                somma += int(n)
        break
    except:
        print("Devi inserire un numero di quattro cifre")


print("La somma è", somma)
