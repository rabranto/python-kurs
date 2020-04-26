"""
Zadanie 3 – sortowanie liczb
Trzy dowolne liczby zapisz do trzech zmiennych.
Znajdź największą liczbę.
Wyświetl liczby od największej do najmniejszej.
"""
x = input("Podaj dowolną liczbę x = ")
y = input("Podaj dowolną liczbę y = ")
z = input("Podaj dowolną liczbę z = ")

if x > y and x > z:
    max = x
elif y > x and y > z:
    max = y
else:
    max = z
print("Podałeś liczby", x , y , z)
print("Najwyższa liczba podana przez Ciebie to", max)
print("Następuje sortowanie liczb od największej do najmniejszej")
'''
 x y z
 1 2 3
 jesli x jest mniejsze od y niech x zamieni sie miejscem z y
 y x z
 2 1 3
 jesli x jest mniejsze od z niech x zamieni sie miejscem z z
 y z x
 2 3 1
 jesli y jest mniejsze od z niech y zamieni sie miejsce z z
 z y x
 3 2 1
 '''
if x < y:
    temp = x
    x = y
    y = temp
print("Sortowanie...", x , y , z)
if x < z:
    temp = x
    x = z
    z = temp
print("Sortowanie...",x,y,z)
if y < z:
    temp = y
    y = z
    z = temp
print("Sortowanie...",x,y,z)



