"""
Zadanie 5 - twierdzenie Pitagorasa
a) Poproś użytkownika o podanie długości boków A, B i C i sprawdź czy w ogóle możliwe jest
utworzenie z nich trójkąta 🙂
b) Odpowiedz czy trójkąt jest trójkątem pitagorejskim.
c) Szczególnym przypadkiem jest trójkąt egipski o stosunkach długości 3:4:5.
Sprawdź czy trójkąt pitagorejski jest trójkątem egipskim.
d) Uwzględnij, że kolejność danych nie musi mieć znaczenia! 
"""
A = int(input("Podaj długość boku A = "))
B = int(input("Podaj długość boku B = "))
C = int(input("Podaj długość boku C = "))

print("Sprawdźmy czy możemy z tych boków zrobić trójkąt...")

if A > B:
    temp = A
    A = B
    B = temp
if A > C:
    temp = A
    A = C
    C = temp
if B > C:
    temp = B
    B = C
    C = temp
'''
 A B C
jesli A jest wieksze od B to niech A zamieni sie miejscem z B
BAC
jesli A jest wieksze dd C to niech A zamieni sie miejscami z C
BCA
jesli B jest wieksze od C to niech B zmiani sie miejscami z C
CBA 
 '''
print("Sprawdzam trójkąt", A, B, C)
"""
Trójkąt powstanie gdy a + b > c
"""
is_triangle = False
if A + B > C:
    print("Jest możliwość utworzniea trójkąta")
    is_triangle = True
else:
    print("Brak możliwości utworzenia trójkąta.")

if is_triangle and A**2 + B**2 == C**2:
    print("Powstał trójkąt pitagorejski")
    if A/3 == B/4 == C/5:
        print("Ponadto szczególny przypadek - trójkąt egipski")
elif is_triangle:
    print("Utworzono trójkąt")

