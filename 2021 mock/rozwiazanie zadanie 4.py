wyniki1 = open('wyniki4_1.txt', 'w')
wyniki2a = open('wyniki4_2a.txt', 'w')
wyniki2b = open('wyniki4_2b.txt', 'w')
wyniki3 = open('wyniki4_3.txt', 'w')

with open('galerie.txt', 'r') as galerie_plik:
# with open('galerie_przyklad.txt', 'r') as galerie_plik:
    kraje = []
    miasta = []
    lokale = []
    for linia in galerie_plik:
        linia = linia.strip().split(' ')
        kraje.append(linia[0])
        miasta.append(linia[1])
        lokale.append([(int(linia[i]), int(linia[i+1])) for i in range(2, len(linia), 2) if int(linia[i]) != 0])

def zadanie_1(kraje):
    dict_kraje = {kraj:0 for kraj in kraje}
    for kraj in kraje:
        dict_kraje[kraj] += 1
    for kraj, liczba_miast in dict_kraje.items():
        # print(kraj, liczba_miast)
        wyniki1.write(f'{kraj} {liczba_miast}\n')

def zadanie_2(miasta, lokale):

    def powierzchnia(lokale):
        powierzchnia = 0
        for x_y in lokale:
            x = x_y[0]
            y = x_y[1]
            powierzchnia += x * y
        return powierzchnia

    max_powierzchnia = 0
    max_miasto = ''
    min_powierzchnia = powierzchnia(lokale[0])
    min_miasto = ''

    for miasto, lokal in zip(miasta, lokale):
        # print(miasto, powierzchnia(lokal), len(lokal))
        powierzchnia_wartosc = powierzchnia(lokal)
        wyniki2a.write(f'{miasto} {powierzchnia_wartosc} {len(lokal)}\n')

        if powierzchnia_wartosc > max_powierzchnia:
            max_powierzchnia = powierzchnia_wartosc
            max_miasto = miasto
        if powierzchnia_wartosc < min_powierzchnia:
            min_powierzchnia = powierzchnia_wartosc
            min_miasto = miasto

    wyniki2b.write(f'{max_miasto} {max_powierzchnia}\n'
                   f'{min_miasto} {min_powierzchnia}')

def zadanie_3(miasta, lokale):

    def liczba_unikatowych_lokali(lokale):
        tab_powierzchnia = [x[0] * x[1] for x in lokale]
        tab_powierzchnia = set(tab_powierzchnia)
        return len(tab_powierzchnia)

    max_miasto = ''
    max_rozne_lokale = 0
    min_miasto = ''
    min_rozne_lokale = liczba_unikatowych_lokali(lokale[0])

    for miasto, lokal in zip(miasta, lokale):
        rozne_lokale_wartosc = liczba_unikatowych_lokali(lokal)
        if rozne_lokale_wartosc > max_rozne_lokale:
            max_rozne_lokale = rozne_lokale_wartosc
            max_miasto = miasto
        if rozne_lokale_wartosc < min_rozne_lokale:
            min_rozne_lokale = rozne_lokale_wartosc
            min_miasto = miasto
    # print(max_miasto, max_rozne_lokale, min_miasto, min_rozne_lokale)
    wyniki3.write(f'{max_miasto} {max_rozne_lokale}\n'
                  f'{min_miasto} {min_rozne_lokale}')

if __name__ == '__main__':
    zadanie_1(kraje)
    zadanie_2(miasta, lokale)
    zadanie_3(miasta, lokale)
