ilosc_prob = 5
haslo = "okon"
proba = 1
podane_haslo = ""
while proba <= 5:
    print("Zgadnij haslo:")
    podane_haslo = input()
    if haslo.lower() == podane_haslo.lower():
        print("Odgadnieto haslo!")
        break
    proba += 1
    if proba == ilosc_prob+1:
        print("no niestety")
