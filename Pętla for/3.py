"""
Zadanie 3
Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
(np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
Następnie powitaj każdą osobę na liście.
"""

name = input("Wprowadź dowolną liczbę imion ciągiem, oddzielonych przecinkiem lub białym'\
znakiem(np. Radek, Marek, Arek): ")
name = name.title()
name = name.split(',')

for i in name:
    for j in i.split():
        print("Witaj " + j)



