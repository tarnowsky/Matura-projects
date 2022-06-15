wyniki = open('wyniki4.txt', 'w')

file = open('punkty.txt', 'r')
wiersze = file.readlines()
punkty = [[int(x) for x in x_y.strip().split(' ')] for x_y in wiersze]

#zadanie 1
def czy_pierwsza(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

wynik = 0
for x_y in punkty:
    if czy_pierwsza(x_y[0]) and czy_pierwsza(x_y[1]):
        wynik += 1
wyniki.write(f'ZADANIE 4.1\n{wynik}\n\n')

#zadanie 2
wynik = 0
for x_y in punkty:
    if set(str(x_y[0])) == set(str(x_y[1])):
        wynik += 1
wyniki.write(f'ZADANIE 4.2\n{wynik}\n\n')

#zadanie 3
def odleglosc_punktow(x_y1,x_y2):
    d = ((x_y1[0]-x_y2[0])**2 + (x_y1[1]-x_y2[1])**2)**0.5
    return round(d)

max_odleglosc = 0
index = -1
for x_y1 in punkty:
    index += 1
    for i in range(len(punkty)):
        if i == index:
            continue
        x_y2 = punkty[i]
        odleglosc = odleglosc_punktow(x_y1, x_y2)
        if odleglosc > max_odleglosc:
            max_odleglosc = odleglosc
            max_wspolrzedne = [x_y1, x_y2]
wyniki.write(f'ZADANIE 4.3\n'
             f'odległość: {max_odleglosc}\n'
             f'współrzędne punktów: {max_wspolrzedne[0]} {max_wspolrzedne[1]}\n\n')

#zadanie 4
def punkt_do_kwadratu(x_y):
    x, y = x_y[0], x_y[1]
    #wnetrze
    if x < 5_000 and y < 5_000:
        return 0
    # zewnetrze
    if x > 5_000 or y > 5_000:
        return 1
    #krawedz
    return 2

wnetrze = 0
zewnetrze = 0
krawedz = 0
for x_y in punkty:
    wynik = punkt_do_kwadratu(x_y)
    if wynik == 0:
        wnetrze += 1
    if wynik == 1:
        zewnetrze += 1
    if wynik == 2:
        krawedz += 1
wyniki.write(f'ZADANIE 4.4\n'
             f'wnetrze: {wnetrze}\n'
             f'krawędź: {krawedz}\n'
             f'zewnętrze: {zewnetrze}')
