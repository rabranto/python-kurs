"""
Zadanie 1 – rozgrzewka
Podpunktów nie trzeba wykonywać pokolei, jeśli czegoś nie pamietasz – idź dalej. Możesz przeczytać wpis ponownie i wrócić do pozostawionego zadania

Do zmiennej sentence przypisz zdanie: „Kurs Pythona jest prosty i przyjemny.”,
a następnie:

Policz wszystkie znaki w napisie
Nie modyfikując zmiennej sentence wyświetl słowo „prosty”
Wyświetl znak o indeksie (czy za każdym razem rozumiesz co się dzieje?):
a)7
b)12
c)-4
d)37
Wprowadź do zdania 2 błędy ortograficzne 😉
"""
print("*" * 20)
print("Zadanie 1 - rozgrzewka")
print("*" * 20)
sentence = "Kurs Pythona jest prosty i przyjemny."
print(sentence)
print("Przypisano wartość do zmiennej \'sentence\'")
print('Ilość wszystkich znaków w napisie to: ',len(sentence))
print("Wyświetlono słowo \'prosty\' nie modyfikując zmiennej:",sentence[18:24])
print("Znak o indeksie a)7: ", sentence[7])
print("Znak o indeksie b)12: ", sentence[12])
print("Znak o indeksie c)-4: ", sentence[-4])
print("Znak o indeksie d)37: \"Brak możliwości wyświetlenia znaku o indeksie 37 - nie istnieje\"")
print("Dodano 2 błędy ortograficzne w zmiennej \'sentence\'")
sentence = sentence.replace("jest", "jezd")
sentence = sentence.replace("rz", "sz")
print(sentence)
"""
Zadanie 2
Utwórz skrypt, który zapyta użytkownika o imię, nazwisko i numer telefonu, a następnie:

Sprawdź czy imię i nazwisko składają się tylko z liter, a nr tel składa się wyłącznie z cyfr (wyświetl tę informację jako true/false)
Użytkownicy bywają leniwi. Nie zawsze zapisują imię czy nazwisko z dużej litery – popraw ich
Niektórzy podają numer telefonu z myślnikami lub z spacjami, usuń zbędne znaki z numeru
Zakładając, że twoi użytkownicy noszą polskie imiona, sprawdź czy użytkownik jest kobietą
Połącz dane w jeden ciąg personal za pomocą spacji
Policz liczbę wszystkich znaków w napisie personal
Podaj liczbę tylko liter w napisie personal[hint]
[hint]Podpowiedź – weź pod uwagę, że numery telefonów w Polsce są 9-cyfrowe
"""
print("*" * 20)
print("Zadanie 2 - utwórz skrypt")
print("*" * 20)
name = input("Jak masz na imię?: ")
surname = input("Jak masz na nazwisko?: ")
tel = input("Podaj numer telefonu: ")
print("Wszystkie znaki w Twoim imieniu są literami?:", name.isalpha())
print("Wszystkie znaki w Twoim nazwisku są literami?:",surname.isalpha())
print("Wszystkie znaki w Twoim numerze telefonu są cyframi?:",tel.isdigit())
name = name.title()
surname = surname.title()
tel = tel.replace("+","")
tel = tel.replace("-","")
tel = tel.replace(" ","")
personal = name + " " + surname +" "+ tel
length = len(personal)
print("Stworzono zmienną personal, która zawiera wszystkie wprowadzone informacje:", personal)
print("Liczba znaków w personal: ", length)
print("Liczba liter w personal: ",length-11)
