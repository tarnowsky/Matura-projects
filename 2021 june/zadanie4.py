with open('napisy.txt', 'r') as file:
# with open('przyklad.txt', 'r') as file:
    napisy = file.readlines()
    napisy = [x.strip() for x in napisy]

LITERY = [chr(i) for i in range(65, 91)]
CYFRY = [str(i) for i in range(10)]

cyfry_z_napisow = [[cyfra for cyfra in napis if cyfra in CYFRY] for napis in napisy]

def zadanie_4_1(tab):
    liczba_cyfr = 0
    for napis in tab:
        for znak in napis:
            if znak in CYFRY:
                liczba_cyfr += 1
    return liczba_cyfr

def zadanie_4_2(tab):
    nr_indeksu_litery = 0
    w = ''
    for i, napis in enumerate(tab):
        if i != 0 and (i+1) % 20 == 0:
            w += napis[nr_indeksu_litery]
            nr_indeksu_litery += 1
    return w

def zadanie_4_3(tab):
    global LITERY, CYFRY
    tab_znakow = LITERY + CYFRY
    w = ''
    for napis in tab:
        for znak in tab_znakow:
            potencjalny_palindrom_1 = znak + napis
            potencjalny_palindrom_2 = napis + znak
            if potencjalny_palindrom_1 == potencjalny_palindrom_1[::-1]:
                w += potencjalny_palindrom_1[25]
            elif potencjalny_palindrom_2 == potencjalny_palindrom_2[::-1]:
                w += potencjalny_palindrom_2[25]
    return w

def zadanie_4_4(tab):
    w = ''
    for cyfry in tab:
        if cyfry:
            n = len(cyfry)
            if n > 1:
                if n % 2 == 1:
                    n -= 1
                liczby = []
                liczba = []
                for x in range(n):
                    liczba += cyfry[x]
                    if x != 0 and (x + 1) % 2 == 0:
                        liczby += [''.join(liczba)]
                        liczba = []
                for liczba in liczby:
                    if 65 <= int(liczba) <= 90:
                        w += chr(int(liczba))
                if w[-3:] == 'XXX':
                    return w

with open('wyniki4.txt', 'w') as wyniki:
    wyniki.write('ZADANIE 4.1.\n')
    wyniki.write(f'{zadanie_4_1(napisy)}\n\n')
    wyniki.write('ZADANIE 4.2.\n')
    wyniki.write(f'{zadanie_4_2(napisy)}\n\n')
    wyniki.write('ZADANIE 4.3.\n')
    wyniki.write(f'{zadanie_4_3(napisy)}\n\n')
    wyniki.write('ZADANIE 4.4.\n')
    wyniki.write(f'{zadanie_4_4(cyfry_z_napisow)}')
