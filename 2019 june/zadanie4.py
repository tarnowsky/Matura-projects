#--------------PRZYGOTOWANIE PLIKÓW WYNIKÓW---------------
WYNIKI_1 = open('wyniki4_1.txt', 'w')
WYNIKI_2 = open('wyniki4_2.txt', 'w')
WYNIKI_3 = open('wyniki4_3.txt', 'w')

#--------------WCZYTANIE PLIKÓW ZADAŃ---------------
file_liczby = open('liczby.txt', 'r')
# file_liczby = open('liczby_przyklad.txt', 'r')
file_pierwsze = open('pierwsze.txt', 'r')
# file_pierwsze = open('pierwsze_przyklad.txt', 'r')

wiersze_liczby = file_liczby.readlines()
wiersze_pierwsze = file_pierwsze.readlines()

tab_liczby = [int(wiersz.strip()) for wiersz in wiersze_liczby]
tab_pierwsze = [int(wiersz.strip()) for wiersz in wiersze_pierwsze]

#--------------ZADANIA 1, 2, 3---------------
def czy_pierwsza(liczba):
    if liczba == 2:
        return True
    if liczba < 2 or liczba % 2 == 0:
        return False
    for i in range(3, int(liczba**0.5)+1):
        if liczba % i == 0:
            return False
    return True

def w(N):
    if len(str(N)) == 1:
        return N
    tab_cyfry = [int(cyfra) for cyfra in str(N)]
    return w(sum(tab_cyfry))

for liczba in tab_liczby:
    if 100 < liczba < 5_000:
        if czy_pierwsza(liczba):
            # print(liczba, end=' ')
            WYNIKI_1.write(f'{liczba}\n')

licznik_zad_3 = 0
for pierwsza in tab_pierwsze:
    if czy_pierwsza(int(str(pierwsza)[::-1])):
        # print(pierwsza, end=' ')
        WYNIKI_2.write(f'{pierwsza}\n')
    if w(pierwsza) == 1:
        licznik_zad_3 += 1
# print(licznik_zad_3)
WYNIKI_3.write(f'{licznik_zad_3}')




