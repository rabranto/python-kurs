"""
Zadanie 4
Napisz prosty program, który wykona się zadaną przez użytkownika liczbę razy.
Z każdym uruchomieniem pętli wyświetli informacje:
– czy liczba jest wielokrotnością 3
– czy liczba jest wielkorotnością 4
– wyświtli „hurra” jeżeli liczba dzieli się zarówno przez 3 jak i 4
– wyświetli gwiazdkę, jeśli żaden z powyższych warunków nie jest spełniony
"""
y = int(input("Ile razy ma się wykonać program? "))
"""
Czy liczba jest wielokrotnością 3
x/3
oznacza to, że liczba jest podzielna przez 3 z resztą 0
x % 3
"""
for i in range(y):
    x = int(input("Podaj losową liczbę... "))
    if ((x % 3 == 0) & (x % 4 == 0)):
        print("Hurra! Liczba jest wielkrotnością 3 i 4.")
    elif x % 3 == 0:
        print("Liczba jest wielokrotnością 3.")
    elif x % 4 == 0:
        print("Liczba jest wielokrotnością 4.")
    else:
        print("*")
    
