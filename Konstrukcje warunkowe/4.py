"""
Zadanie 4 – imiona
Utwórz zbiór imion męskich i żeńskich. Poproś użytkownika o podanie imienia.
Sprawdź czy imię jest męskie czy żeńskie i wyświetl na ten temat informację.
Jeżeli imienia nie ma na liście wyświetl komunikat „Nie znamy tego imienia.”
Następnie użytkownik poda informację czy imię jest męskie czy żeńskie.
Dodaj imię do listy.
"""
print('*'*125)
names = {"Wiktoria": "żeńskie", "Wioleta": "żeńskie", "Radek": "męskie", "Marlena": "żeńskie", "Krzysztof": "męskie","Andrzej":"męskie","Barbara":"żeńskie", "Damian": "męskie", "Albert": "męskie", "Linda":"żeńskie", "Oskar":"męskie", "Gracjan": "męskie"}
print(list(names.keys()))
print('*'*125)
name = input("Podaj swoje imię: ")
name = name.title()
if name in names.keys():
    print("To jest imię",names[name])
else:
    print("Nie znamy tego imienia.")
    sex = input("Jest to imię męskie czy żeńskie? ")
    names[name] = sex
    print("Zaaktualizowano baze imion.")
    print('*'*125)
    print(list(names.keys()))
    print('*'*125)

