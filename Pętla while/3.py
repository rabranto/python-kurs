"""
Zadanie 3
Stwórz prostą grę zgadywankę. Komputer losuje wartość z przedziału od 1-30.
Poproś użytkownika o zgadnięcie liczby. Program pyta użytkownika o podanie
liczby tak długo, dopóki gracz nie zgadnie.
Gracz powinen otrzymać informację czy jego liczba jest za duża czy za mała.
"""
import random
secret_number = random.randint(0, 30)
number = int(input("Zgadnij liczbę z przedziału 1 - 30 "))
if number < secret_number:
    print("Liczba jest za mała.")
elif number > secret_number:
    print("Liczba jest za duża.")
while number != secret_number:
    number = int(input("To nie jest ta liczba! Spróbuj jeszcze raz "))
    if number < secret_number:
        print("Liczba jest za mała.")
    elif number > secret_number:
        print("Liczba jest za duża.")
print("Brawo!")
    
