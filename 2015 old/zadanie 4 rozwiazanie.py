with open('slowa.txt', 'r') as file:
    wiersze = file.readlines()
    wiersze_wiecej_0 = 0
    wiersze_2_bloki = 0
    max_dl_bloku_zer = 0
    wiersze_tab = []

    def ile_blokow(a:str):
        liczba_blokow = 1
        for i in range(len(a)-1):
            aktualna_lit = a[i]
            nastepna_lit = a[i+1]
            if aktualna_lit == nastepna_lit:
                continue
            else: liczba_blokow += 1
        if a[0] == '0' and liczba_blokow == 2:
            return True
        return False

    def dlugosc_bloku_zer(a:str):
        max_dl = 0
        aktualna_dl = 0
        for i in range(len(a)-1):
            aktualna_lit = a[i]
            nastepna_lit = a[i+1]
            if aktualna_lit == '0':
                if aktualna_dl == 0:
                    aktualna_dl = 1
                if nastepna_lit == '0':
                    aktualna_dl += 1
            if aktualna_dl > max_dl:
                max_dl = aktualna_dl
            if aktualna_lit != nastepna_lit:
                aktualna_dl = 0
        return max_dl

    for wiersz in wiersze:
        jedynki = zera = 0
        wiersz = wiersz.strip()
        wiersze_tab.append(wiersz)
        dl_bloku_zer = dlugosc_bloku_zer(wiersz)
        if dl_bloku_zer > max_dl_bloku_zer:
            max_dl_bloku_zer = dl_bloku_zer
        if ile_blokow(wiersz):
            wiersze_2_bloki += 1
        for num in wiersz:
            if num == '1':
                jedynki += 1
            else:
                zera += 1
        if zera > jedynki:
            wiersze_wiecej_0 += 1

with open('wyniki4.txt', 'w') as wyniki:
    wyniki.write(f'ZADANIE 4.1\n'
                 f'{wiersze_wiecej_0}\n\n')
    wyniki.write(f'ZADANIE 4.2\n'
                 f'{wiersze_2_bloki}\n\n')
    wyniki.write(f'ZADANIE 4.3\n'
                 f'{max_dl_bloku_zer}\n')
    for wiersz in wiersze_tab:
        if dlugosc_bloku_zer(wiersz) == max_dl_bloku_zer:
            wyniki.write(f'{wiersz}\n')
