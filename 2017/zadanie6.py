from pprint import pprint

wyniki = open('wyniki6.txt','w')

file = open('dane.txt', 'r')
# file = open('przyklad.txt', 'r')

wiersze = file.readlines()
piksele_tab = [wiersz.strip().split(' ') for wiersz in wiersze]
for i in range(len(piksele_tab)):
    for j in range(len(piksele_tab[i])):
        piksele_tab[i][j] = int(piksele_tab[i][j])

#zadanie 1
max_piksel_0 = 0
min_piksel_0 = 300
for i in piksele_tab:
    max_piksel = max(i)
    min_piksel = min(i)
    if max_piksel > max_piksel_0:
        max_piksel_0 = max_piksel
    if min_piksel < min_piksel_0:
        min_piksel_0 = min_piksel
# print(max_piksel_0, min_piksel_0)
wyniki.write(f'ZADANIE 6.1\nnajjaśniejszy piksel: {max_piksel_0}\nnajciemniejszy piksel: {min_piksel_0}\n\n')

#zadanie 2
wynik = 0
for i in piksele_tab:
    if i != i[::-1]:
        wynik += 1
# print(wynik)
wyniki.write(f'ZADANIE 6.2\n{wynik}\n\n')

#zadanie 3
def czy_kontrastujące(a,b):
    if abs(a-b) > 128:
        return True
    return False

wynik = 0
for i in range(len(piksele_tab)):
    for j in range(len(piksele_tab[i])):
        if i == 0:
            if j == 0:
                if czy_kontrastujące(piksele_tab[i][j], piksele_tab[i][j+1])\
                        or czy_kontrastujące(piksele_tab[i][j], piksele_tab[i+1][j]):
                    wynik += 1
            if j == 319:
                if czy_kontrastujące(piksele_tab[i][j], piksele_tab[i][j-1])\
                        or czy_kontrastujące(piksele_tab[i][j], piksele_tab[i+1][j]):
                    wynik += 1
            else:
                if czy_kontrastujące(piksele_tab[i][j], piksele_tab[i][j-1])\
                        or czy_kontrastujące(piksele_tab[i][j], piksele_tab[i][j+1])\
                        or czy_kontrastujące(piksele_tab[i][j], piksele_tab[i+1][j]):
                    wynik += 1
        elif i == 199:
            if j == 0:
                if czy_kontrastujące(piksele_tab[i][j], piksele_tab[i][j + 1]) \
                        or czy_kontrastujące(piksele_tab[i][j], piksele_tab[i - 1][j]):
                    wynik += 1
            if j == 319:
                if czy_kontrastujące(piksele_tab[i][j], piksele_tab[i][j - 1]) \
                        or czy_kontrastujące(piksele_tab[i][j], piksele_tab[i - 1][j]):
                    wynik += 1
            else:
                if czy_kontrastujące(piksele_tab[i][j], piksele_tab[i][j - 1]) \
                        or czy_kontrastujące(piksele_tab[i][j], piksele_tab[i][j + 1]) \
                        or czy_kontrastujące(piksele_tab[i][j], piksele_tab[i - 1][j]):
                    wynik += 1
        elif j == 0:
            if czy_kontrastujące(piksele_tab[i][j], piksele_tab[i-1][j]) \
                    or czy_kontrastujące(piksele_tab[i][j], piksele_tab[i][j + 1]) \
                    or czy_kontrastujące(piksele_tab[i][j], piksele_tab[i + 1][j]):
                wynik += 1
        elif j == 319:
            if czy_kontrastujące(piksele_tab[i][j], piksele_tab[i+1][j]) \
                    or czy_kontrastujące(piksele_tab[i][j], piksele_tab[i][j-1]) \
                    or czy_kontrastujące(piksele_tab[i][j], piksele_tab[i - 1][j]):
                wynik += 1
        elif czy_kontrastujące(piksele_tab[i][j], piksele_tab[i][j-1])\
                or czy_kontrastujące(piksele_tab[i][j], piksele_tab[i][j+1])\
                or czy_kontrastujące(piksele_tab[i][j], piksele_tab[i+1][j])\
                or czy_kontrastujące(piksele_tab[i][j], piksele_tab[i-1][j]):
                    wynik += 1
wyniki.write(f'ZADANIE 3\n{wynik}\n\n')

#zadanie 4
aktualna_dl = 1
max_dl = 0

for kolumna in range(320): #kolumny
    for wiersz in range(200-1): #wiersze (-1 za sprawdzanie wiersza z kolejnym)
        if piksele_tab[wiersz][kolumna] == piksele_tab[wiersz + 1][kolumna]:
            aktualna_dl += 1
        if aktualna_dl > max_dl:
            max_dl = aktualna_dl
        if not piksele_tab[wiersz][kolumna] == piksele_tab[wiersz + 1][kolumna]:
            aktualna_dl = 1
# print(max_dl)
wyniki.write(f'ZADANIE 4\n{max_dl}')







