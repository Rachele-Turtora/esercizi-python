#Crea un array vuoto.
#Chiedi per 6 volte all’utente di inserire un numero,
#Se è dispari inseriscilo nell’array.
#Stampa in console l'array risultante.

array = []

for i in range(1, 7):

    while True:
        try:
            num = int(input(f"{i} di 6 - Inserisci un numero: "))
            break
        except:
            print("Inserisci un numero")

    if num % 2 != 0:
        array.append(num)

print(array)