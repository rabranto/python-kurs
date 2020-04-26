"""
Utwórz spis oglądanych seriali.
Każdy serial powinen mieć przypisaną ocenę w skali od 1-10.
Zapytaj użytkownika jaki serial chce obejrzeć.
W odpowiedzi podaj jego ocenę.
Zapytaj użytkownika o dodanie kolejnego serialu i oceny.
Dodaj serial do spisu.
"""
TV_Series = {"La casa de papel": 9, "Mr. Robot": 8, "Breaking Bad": 7, "Peaky Blinders": 9}
print(list(TV_Series.keys()))
print('********************************************************************************')
title = input('Jaki serial chciałbyś obejrzeć? ')
print('Seiral {} otrzymał ocenę {}' .format(title, TV_Series[title]))
print('********************************************************************************')
new_title = input('Jeśli chcesz dodać nowy serial do spisu, podaj jego tytuł: ')
rating = input('Jak go oceniasz w skali od 1-10? ')
TV_Series[new_title] = rating
print('********************************************************************************')
print("Zaaktualizowana lista seriali: ", list(TV_Series.keys()))

    
      

