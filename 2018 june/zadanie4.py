#---------PLIKI Z WYNIKAMI--------
wyniki1 = open('wynik4_1.txt', 'w')
wyniki2 = open('wynik4_2.txt', 'w')
wyniki3 = open('wynik4_3.txt', 'w')
wyniki4 = open('wynik4_4.txt', 'w')
#---------WCZYTANIE PLIKÓW---------
dane1 = open('dane1.txt', 'r')
dane2 = open('dane2.txt', 'r')
# dane1 = open('przyklad1.txt', 'r')
# dane2 = open('przyklad2.txt', 'r')

wiersze = dane1.readlines()
dane1 = [[int(i) for i in num.strip().split(' ')] for num in wiersze]
wiersze = dane2.readlines()
dane2 = [[int(i) for i in num.strip().split(' ')] for num in wiersze]
#--------ROZWIĄZANIA ZADAŃ----------
#zadanie 1
wynik = 0
for tab_x, tab_y in zip(dane1, dane2):
    if tab_x[-1] == tab_y[-1]:
        wynik += 1
# print(wynik)
wyniki1.write(f'{wynik}')

#zadanie 2
wynik = 0
for tab_x, tab_y in zip(dane1, dane2):
    parzyste_x = 0
    parzyste_y = 0
    for x, y in zip(tab_x, tab_y):
        if x % 2 == 0:
            parzyste_x += 1
        if y % 2 == 0:
            parzyste_y += 1
    if parzyste_x == parzyste_y == 5:
        wynik += 1
# print(wynik)
wyniki2.write(f'{wynik}')

# zadanie 3
wynik = 0
wiersz = 0
wiersze = []
for tab_x, tab_y in zip(dane1, dane2):
    wiersz += 1
    if set(tab_x) == set(tab_y):
        wiersze += [wiersz]
        wynik += 1
# print(wynik, wiersze)
wyniki3.write(f'liczba wierszy: {wynik}\nnr wiersza: {wiersze}')

#zadanie 4
def sort_scal(tab_x, tab_y):
    tab_x.sort()
    tab_y.sort()
    dl_tab_x = len(tab_x)
    dl_tab_y = len(tab_x)
    wynik = []
    index_x = index_y = 0
    while index_x < dl_tab_x and index_y < dl_tab_y:
        if tab_x[index_x] <= tab_y[index_y]:
            wynik += [tab_x[index_x]]
            index_x += 1
        else:
            wynik += [tab_y[index_y]]
            index_y += 1
    if index_x < index_y:
        wynik += tab_x[index_x:]
    else: wynik += tab_x[index_y:]
    return wynik

for tab_x, tab_y in zip(dane1, dane2):
    wyniki4.write(f'{sort_scal(tab_x, tab_y)}\n')
    # print(sort_scal(tab_x, tab_y))

