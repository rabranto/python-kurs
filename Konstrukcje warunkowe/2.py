"""
Zadanie 2 – kalkulator BMI
W poprzednich częściach pisaliśmy kalkulator BMI, teraz wzbogacimy go o interpretację wyniku.
Program powinien sprawdzić czy BMI należy do jednego z 4 wyników:
niedowaga/waga normalna/lekka nadwaga i nadwaga.
Ponadto w przypadku nadwagi chcemy sprawdzić czy mamy doczynienia z otyłością.
"""
print("Podaj mi swój wzrost i wagę, a policzę Ci BMI :) ")
wzrost = int(input("Ile masz wzrostu w centymetrach? "))
waga = int(input("Twoja waga w kilogramach? "))
BMI = (waga / (wzrost ** 2))*10000
print("Twoje BMI wynosi:", round(BMI, 2))
if BMI < 18.5:
    print("Zacznij jeść więcej, masz niedowagę!")
elif 18.5 < BMI < 24:
    print("Spokojnie... U Ciebie wszystko w normie :)")
elif 24 < BMI < 26.5:
    print("Masz lekką nadwagę, czas się troszkę poruszać.")
elif BMI > 26.5:
    print("Zabieraj się do roboty, masz nadwagę...")
elif 30 < BMI < 35:
    print("Otyłość I stopnia")
elif 35 < BMi < 40:
    print("Otyłość II stopnia")
else:
    print("Otyłość III stopnia")

