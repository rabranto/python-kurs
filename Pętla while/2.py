"""
Zadanie 2
Zapoznaj się z modułem random.
>>> import random
Stwórz prostą grę zgadywankę. Komputer losuje wartość z przedziału od 1-30.
Poproś użytkownika o zgadnięcie liczby. Program pyta użytkownika o podanie
liczby tak długo, dopóki gracz nie zgadnie.
"""
import random
secret_number = random.randint(0, 30)
number = int(input("Zgadnij liczbę z przedziału 1 - 30 "))
while number != secret_number:
    number = int(input("To nie jest ta liczba! Spróbuj jeszcze raz "))
print("Brawo!")
    
