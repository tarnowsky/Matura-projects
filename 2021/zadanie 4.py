with open('instrukcje.txt', 'r') as file:
# with open('przyklad.txt', 'r') as file:
    wiersze = file.readlines()
    instrukcje_tab = [wiersz.strip().split() for wiersz in wiersze]

DICT_LITERA_ASCII = {chr(i): i for i in range(65,91)}

def zamiana_litery(a:str, b):
    ile = int(b)
    nowa_litera = ord(a) + ile
    if nowa_litera > 90:
        nowa_litera -= 26
    return chr(nowa_litera)

# konstruowanie napisu z polecen z tablicy instrukcji
def konstruuj_napis(tab:list):
    napis = []
    for insturkcja_lit in tab:
        polecenie = insturkcja_lit[0]
        litera = insturkcja_lit[1]
        if polecenie == 'DOPISZ':
            napis += [litera]
        if polecenie == 'ZMIEN':
            napis[-1] = litera
        if polecenie == 'USUN':
            napis.pop()
        if polecenie == 'PRZESUN':
            napis[napis.index(litera)] = zamiana_litery(litera, 1)
    napis = ''.join(napis)
    return napis

#ZADANIE 2
def najdluzszy_ciag_instrukcji(tab):
    max_instrukcja = ''
    max_instrukcja_wystapienia = 0
    aktualna_instrukcja_wystapienia = 1
    for i in range(len(tab)-1):
        instrukcja = tab[i][0]
        nastepna_instrukcja = tab[i+1][0]
        if instrukcja == nastepna_instrukcja:
            aktualna_instrukcja_wystapienia += 1
        if aktualna_instrukcja_wystapienia > max_instrukcja_wystapienia:
            max_instrukcja = instrukcja
            max_instrukcja_wystapienia = aktualna_instrukcja_wystapienia
        if instrukcja != nastepna_instrukcja:
            aktualna_instrukcja_wystapienia = 1
    return max_instrukcja, max_instrukcja_wystapienia

def najczesciej_dopisywana(tab):
    dict_litery_wystapienia = {i: 0 for i in DICT_LITERA_ASCII.keys()}
    for instrukcja_litera in tab:
        if not instrukcja_litera[0] == 'DOPISZ':
            continue
        litera = instrukcja_litera[1]
        dict_litery_wystapienia[litera] += 1
    max_litera_wystapienia = max(dict_litery_wystapienia.values())
    max_litera = list(dict_litery_wystapienia.keys())[list(dict_litery_wystapienia.values()).index(max_litera_wystapienia)]
    return max_litera, max_litera_wystapienia

with open('wyniki4.txt', 'w') as wyniki:
    wyniki.write(f'ZADANIE 4.1.\n{len(konstruuj_napis(instrukcje_tab))}\n\n')
    wyniki.write(f'ZADANIE 4.2\n{najdluzszy_ciag_instrukcji(instrukcje_tab)[0]} {najdluzszy_ciag_instrukcji(instrukcje_tab)[1]}\n\n')
    wyniki.write(f'ZADANIE 4.3\n{najczesciej_dopisywana(instrukcje_tab)[0]} {najczesciej_dopisywana(instrukcje_tab)[1]}\n\n')
    wyniki.write(f'ZADANIE 4.4\n{konstruuj_napis(instrukcje_tab)}')

