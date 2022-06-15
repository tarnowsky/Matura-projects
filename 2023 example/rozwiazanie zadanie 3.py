# with open('liczby.txt') as liczby_file:
with open('liczby_przyklad.txt') as liczby_file:
    liczby = liczby_file.readlines()
    liczby = [[int(x) for x in liczba.strip().split()] for liczba in liczby]

def pierwsza(a):
    if a == 2:
        return True
    if a < 2 or a % 2 == 0:
        return False
    for i in range(3, int(a**0.5)+1, 2):
        if a % i == 0:
            return False
    return True

def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, a%b)

#zadanie 1
ile_wierszy_m_pierwsza = 0
ile_wzglegnie_pierwszych = 0

#zadanie 3
odpowiedz = 0
for Mab in liczby:
    #zadanie 1
    if pierwsza(Mab[0]):
        ile_wierszy_m_pierwsza += 1
    #zadanie 2
    if nwd(Mab[0], Mab[1]) == 1:
        ile_wzglegnie_pierwszych += 1
    #zadanie 3
