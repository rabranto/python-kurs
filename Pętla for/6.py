"""
Zadanie 6
Wyświetl w konsoli klasyczną tabliczkę mnożenia.
1 x 1
1 x 2
1 x 3
1 x 4
1 x 5
1 x 6
1 x 7
1 x 8
1 x 9
1 x 10
"""
print('*' * 20)
print("|Tabliczka mnożenia|")
print('*' * 20)
for i in range(1,11):
    for j in range(1,11):
        print('|{:3}  x {:3}  = {:3} |'.format(i,j,i*j))
        if j==10:
            print('*' * 20)
