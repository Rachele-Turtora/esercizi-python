#Il programma dovrà chiedere all'utente il numero di chilometri che vuole percorrere e l'età del passeggero.
#Sulla base di queste informazioni dovrà calcolare il prezzo totale del viaggio, secondo queste regole:
#il prezzo del biglietto è definito in base ai km (0.21 € al km)
#va applicato uno sconto del 20% per i minorenni
#va applicato uno sconto del 40% per gli over 65.
#L'output del prezzo finale va messo fuori in forma umana (con massimo due decimali, per indicare centesimi sul prezzo).


while True:
    try:
        km = int(input("Quanti chilometri devi percorrere? "))
        età = int(input("Quanti anni hai? "))
        break
    except:
        print("Inserisci dei numeri")

prezzo = km * 0.21

if età < 18:
    prezzo = (prezzo * 80) / 100
elif età > 65:
    prezzo = (prezzo * 60) / 100

print("Il prezzo del tuo biglietto è:", round(prezzo, 2))
