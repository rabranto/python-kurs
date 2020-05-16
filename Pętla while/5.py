"""
Zadanie 5
Korzystając z modułu random stwórz kolejną prostą grę.
Komputer losuje słowo z dostępnego zakresu (posiada listę słów).
Następnie litery są mieszane. Wymieszane litery pokazywane są graczowi.
Gracz musi zgadnąć co to za słowo. Gracz zgaduje do skutku.
Dopiero zgadnięcie przerywa grę.
Rozszerzenie: gracz może wybrać na klawiaturze „q” lub „Q”, aby zakończyć grę
przed czasem.
"""
import random

words = ["wąż", "jest", "fajny", "słówka", "gra", "python"]
lottery = random.choice(words)
mixed_word = ''.join(random.sample(lottery, len(lottery)))
print(mixed_word)
mystery_word = input("Co to jest za słowo? ")
while mystery_word not in words:
    if mystery_word == "q" or "Q":
        print("Dowidzenia!")
        break
    else:
        mystery_word = input("To nie jest to słowo. Spróbuj jeszcze raz. ")
print("Super!")
