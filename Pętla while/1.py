"""
Zadanie 1
Napisz program z wykorzystaniem pętli while, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
"""
i = 0
j = 0
while i < 10:
    i += 1
    j += i
    print(j)
