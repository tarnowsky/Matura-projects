with open('punkty.txt', 'r') as punkty_file, open('okregi.txt', 'r') as okregi_file:
    punkty, okregi = punkty_file.readlines(), okregi_file.readlines()
    punkty = [[float(x) for x in x_y.strip().split()] for x_y in punkty]
    okregi = [[int(x) for x in x_y_r.strip().split()] for x_y_r in okregi]


wynik1 = open('wyniki1.txt', 'w')
wynik2 = open('wyniki2.txt', 'w')
wynik3 = open('wyniki3.txt', 'w')

#zadanie 1
def cwiartka(x, y):
    if x > 0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 2
    if x < 0 and y < 0:
        return 3
    if x > 0 and y < 0:
        return 4

cwiartki = {i: 0 for i in range(1, 5)}
for punkt in punkty:
    x, y = punkt[0], punkt[1]
    cwiartki[cwiartka(x, y)] += 1
for liczba_w_cw in cwiartki.values():
    wynik1.write(f'{liczba_w_cw} ')

#zadanie 2
def styczna(y, r):
    if abs(y) == r:
        return True
    return False

okregi_styczne = [okrag for okrag in okregi if styczna(okrag[1], okrag[2])]
n = len(okregi_styczne)
zamiana = False
while n > 0:
    for i in range(len(okregi_styczne[:n])-1):
        if okregi_styczne[i][0] >= okregi_styczne[i+1][0]:
            if okregi_styczne[i][0] == okregi_styczne[i+1][0]:
                if okregi_styczne[i][1] < okregi_styczne[i+1][1]:
                    okregi_styczne[i], okregi_styczne[i+1] = okregi_styczne[i+1], okregi_styczne[i]
                    zamiana = True
            else:
                okregi_styczne[i], okregi_styczne[i+1] = okregi_styczne[i+1], okregi_styczne[i]
                zamiana = True
    n -= 1
    if not zamiana:
        break
for x in okregi_styczne:
    wynik2.write(f'{x[0]} {x[1]} {x[2]}\n')
wynik2.write(f'{len(okregi_styczne)}')




# zadanie 3
def pole_trojkata(xa, ya, xb, yb):
    return 0.5 * abs(xa*yb - xb*ya)

pole_calkowite = 0
for i, x_y in enumerate(punkty[:-1]):
    pole_calkowite += pole_trojkata(x_y[0], x_y[1], punkty[i+1][0], punkty[i+1][1])
pole_calkowite += pole_trojkata(punkty[-1][0], punkty[-1][1], punkty[0][0], punkty[0][1])
wynik3.write(f'{int(pole_calkowite)}')


