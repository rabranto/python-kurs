"""
Zadanie 4
Napisz skrypt obliczający wartość silnii. Rozwiąż zadanie za pomocą
pętli for oraz pętli while.
Wejście: „Podaj dowolną liczbę całkowitą do 15:” 4
Wyjście: 4! = 24
4! = 1*2*3*4 = 24
"""
x = int(input("Podaj dowolną liczbę całkowitą do 15: "))
while x > 15:
    x = int(input("Podaj dowolną liczbę całkowitą do 15: "))
y = x
for i in range(1, x):
    x *= i
print("{}! = {}".format(y, x))  

    
