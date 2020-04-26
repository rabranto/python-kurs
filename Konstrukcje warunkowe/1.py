"""
Zadanie 1 – pojawiło się powyżej
Skrypt zapyta użytkownika o wiek. Jeżeli użytkownik jest przed 18 wyświetli informację
„Użytkownik niepełnoletni” oraz zwróci ile lat zostało użytkownikowi do pełnoletności.
Użytkownikom pełnoletnim wyświetli informację „Użytkownik pełnoletni”.
Sprawdź czy wiek użytkownika nie przekracza 100 lat i wyświetl komunikat „200 lat ♫”
"""
print("Ile masz lat?")
age = int(input())
left = 18 - age
if age > 100:
    print("200 lat ♫")
elif age >= 18:
    print("Użytkownik pełnoletni")
else:
    print("Użytkownik niepełnoletni. Brakuje Ci {} lat.".format(left))
