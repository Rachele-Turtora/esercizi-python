#Chiedi all’utente la sua email,
#controlla che sia nella lista di chi può accedere,
#stampa un messaggio appropriato sull’esito del controllo.

lista_mails = ["harrypotter@gmail.com", "hermionegranger@yahoo.it", "ronweasley@gmail.com", "dracomalfoy@yahoo.it"]

mail = input("Qual è la tua mail? ")

if mail in lista_mails:
    print("Puoi entrare")
else:
    print("Non puoi entrare")