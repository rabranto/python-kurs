"""
A.Utwórz nowy plik, który po podaniu przez użytkownika
długości w cm będzie wyświetlał wynik w metrach i calach
zaokrąglając do 4 miejsc po przecinku.
B.Podobny skrypt możesz wykonać dla zamiany g na kg.
Wynik wyświetl używając dowolnego sposobu formatowania tekstu.
"""
wide = '*' * 20
print("Exercise 1 \n UNITS")
print(wide)
print("Change cm to m")
length = float(input("Input length in cm: "))
print("Length in centmeters equals: ", length)
print("Length in meters equals: {:.2f}" .format(length/100))
print(wide, "\nChange g to kg")
weight = float(input("Input weight in g: "))
print("Weight in grams equals: ", weight, "\nWieght in kilograms equals: {:.2f}" .format(weight/100))
"""
Napisz skrypt, który, który obliczy stan konta za kilka lat.
Program pyta użytkownika o:
- stan początkowy konta,
- stopę oprocentowania rocznego
- liczbę lat na lokacie
Wynik wyświetl jako zdanie używając dowolnego sposobu formatowania tekstu.
Wypisz np. takie zdanie:
Twoje *stan_początkowy* zł przez *czas* lata na lokacie *oprocentowanie* % urośnie do *wynik*.
"""
print(wide, "\nExercise 2 \n INVESTMENT")
print(wide)
balance = float(input("What is your beginning balance?: "))
interest_rate = int(input("What is interest rate per year?: "))
years = int(input("How many years you want to invest money?: "))
print("Your {} zł after {} years on investment {} % grows til {}" .format(balance, years, interest_rate,((balance * (interest_rate/100))* years)+balance)) 
        

