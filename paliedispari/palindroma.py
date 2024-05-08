#Chiedere all’utente di inserire una parola
#Creare una funzione per capire se la parola inserita è palindroma

word = input("Inserisci una parola: ")

def isPalindroma(input):

    if len(input) == 0: return False
    if len(input) == 1: return True

    start = 0
    end = len(input) - 1

    while start < end:
        if input[start] != input[end]:
            return False
        
        start += 1
        end -= 1

    return True

if isPalindroma(word):
    print(f"{word} è palindroma")
else:
    print(f"{word} non è palindroma")