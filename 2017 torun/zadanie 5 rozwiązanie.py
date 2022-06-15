with open('rejestrator.txt', 'r') as file:
    wiersze = file.readlines()
    rejestrator_tab = [[int(wiersz.strip()[i:i+4], 2) for i in range(0,24,4)] for wiersz in wiersze]
wyniki = open('wyniki5.txt', 'w')

def GGMMSS(tab):
    wynik = ''
    for j, x in enumerate(tab):
        if j != 0 and j % 2 == 0:
            wynik += ':'
        wynik += str(x)
    return wynik

# ZADANIE 1
for i, rejestr in enumerate(rejestrator_tab):
    if i == 1111 - 1 or i == 2222 - 1 or i == 3333 - 1 or i == 4444 - 1:
        wyniki.write(f'{GGMMSS(rejestr)}\n')

wyniki.write('\n')
# ZADANIE 2
def palindrom(tab):
    if tab == tab[::-1]:
        return True
    return False

liczba_palindromow = 0
for rejestr in rejestrator_tab:
    if palindrom(rejestr):
        liczba_palindromow += 1
        wyniki.write(f'{GGMMSS(rejestr)}\n')
wyniki.write(f'{liczba_palindromow}')

wyniki.write('\n')
godziny_liczbaWystapien = {h:0 for h in range(0,24)}
for rejestr in rejestrator_tab:
    godzina = 0
    if rejestr[0] == 0:
        godziny_liczbaWystapien[rejestr[1]] += 1
    else:
        for i, h in enumerate(reversed(rejestr[0:2])):
            godzina += h * 10 ** i
        if godzina == 24:
            godzina = 0
        godziny_liczbaWystapien[godzina] += 1


print(godziny_liczbaWystapien)
