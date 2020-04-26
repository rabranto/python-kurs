# -*- coding: utf-8 -*-
imie = input('Jak masz na imię? ')
print("Cześć",imie,"miło Cię poznać")
wiek = int(input('Ile masz lat? '))
print("Podaj mi swój wzrost i wagę, a policzę Ci BMI :) ")
wzrost = int(input("Ile masz wzrostu w centymetrach? "))
waga = int(input("Twoja waga w kilogramach? "))
BMI = (waga / (wzrost ** 2))*10000
print("Świetnie! Twoje BMI wynosi:", round(BMI, 6),"\nJak podasz mi swoją aktywność fizyczną to powiem Ci jakie masz zapotrzebowanie kaloryczne")
print("Praca siedząca, brak dodatkowej aktywności fizycznej 1.2 \nPraca niefizyczna, mało aktywny tryb życia 1.4 \nLekka praca fizyczna, regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu 1.6 \nPraca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu 1.8 \nPraca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu 2.0")
aktywnosc = float(input("Podaj odpowiednią liczbę w zakresie 1.2 - 2.0: "))
S = 5
PPM = (10 * waga + 6.25 * wzrost - 5 * wiek + S) * aktywnosc
print("Twoje dzienne zapotrzebowanie kaloryczne wynosi:", PPM)
