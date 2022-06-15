def zadanie_1_1(plansza):
    suma_figur_kolumny = [0,0,0,0,0,0,0,0]
    liczba_puste_kolumny = 0
    for rzad in plansza:
        for pole in range(8):
            if rzad[pole] == PUSTE:
                suma_figur_kolumny[pole] += 1
            if suma_figur_kolumny[pole] == 8:
                liczba_puste_kolumny += 1
    return liczba_puste_kolumny

def zadanie_1_2(plansza):
    biale_ilosc = [0]*8
    czarne_ilosc = [0]*8
    for rzad in plansza:
        for pole in rzad:
            if pole != PUSTE:
                if pole in BIALE:
                    pole = BIALE.index(pole)
                    biale_ilosc[pole] += 1
                else:
                    pole = CZARNE.index(pole)
                    czarne_ilosc[pole] += 1
    suma_bierek = [i+j for i, j in zip(biale_ilosc, czarne_ilosc)]
    for i, j in zip(suma_bierek, biale_ilosc):
        if i != 2*j:
            return False
    return True, sum(suma_bierek)

def zadanie_1_3(plansza):
    index_wiezy = 0
    index_krola = 0

    BIALA_WIEZA = 'W'
    CZARNA_WIEZA = 'w'
    BIALY_KROL = 'K'
    CZARNY_KROL = 'k'
    for rzad in plansza:
        if BIALY_KROL in rzad and CZARNA_WIEZA in rzad:
            index_krola = rzad.index(BIALY_KROL)
            index_wiezy = rzad.index(CZARNA_WIEZA)
            for pole in rzad[min(index_krola, index_wiezy) + 1:max(index_krola, index_wiezy)]:
                if pole != PUSTE:
                    break
            else: return True, 'CZARNA'
        if CZARNY_KROL in rzad and BIALA_WIEZA in rzad:
            index_krola = rzad.index(CZARNY_KROL)
            index_wiezy = rzad.index(BIALA_WIEZA)
            for pole in rzad[min(index_krola, index_wiezy) + 1:max(index_krola, index_wiezy)]:
                if pole != PUSTE:
                    break
            else: return True, 'BIALA'

    obrocona_plansza = [[],[],[],[],[],[],[],[],]
    for i, rzad in enumerate(plansza):
        for j, pole in enumerate(rzad):
            obrocona_plansza[j] += [pole]

    for rzad in obrocona_plansza:
        if BIALY_KROL in rzad and CZARNA_WIEZA in rzad:
            index_krola = rzad.index(BIALY_KROL)
            index_wiezy = rzad.index(CZARNA_WIEZA)
            for pole in rzad[min(index_krola, index_wiezy) + 1:max(index_krola, index_wiezy)]:
                if pole != PUSTE:
                    break
            else: return True, 'CZARNA'
        if CZARNY_KROL in rzad and BIALA_WIEZA in rzad:
            index_krola = rzad.index(CZARNY_KROL)
            index_wiezy = rzad.index(BIALA_WIEZA)
            for pole in rzad[min(index_krola, index_wiezy) + 1:max(index_krola, index_wiezy)]:
                if pole != PUSTE:
                    break
            else: return True, 'BIALA'
    return False


with open('szachy.txt', 'r') as szachy_file:
# with open('szachy_przyklad.txt', 'r') as szachy_file:
    szachy = szachy_file.readlines()
    CZARNE = list('kwshgp')
    BIALE = list('KWSHGP')
    PUSTE = '.'
    plansza = []
    #zadanie 1.1
    plansza_pusta_kolumna_liczba = 0
    max_puste_kolumny = 0

    #zadanie 1.2
    plansze_rownowaga = 0
    min_bierki_rownowaga = 1000

    #zadanie 1.3
    biala_czarnego = 0
    czarna_bialego = 0

    for line in szachy:
        line = list(line.strip())
        if line:
            plansza += [line]
        else: plansza = []

        #rozpoczecie pracy nad planszą
        if len(plansza) == 8:
            #zadanie 1
            liczba_pustych_kolumn = zadanie_1_1(plansza)
            if liczba_pustych_kolumn:
                plansza_pusta_kolumna_liczba += 1
                if liczba_pustych_kolumn > max_puste_kolumny:
                    max_puste_kolumny = liczba_pustych_kolumn
            #zadanie 2
            zadanie2 = zadanie_1_2(plansza)
            if zadanie2:
                plansze_rownowaga += 1
                if zadanie2[1] < min_bierki_rownowaga:
                    min_bierki_rownowaga = zadanie2[1]

            #zadanie 3
            zadanie3 = zadanie_1_3(plansza)
            if zadanie3:
                if zadanie3[1] == 'BIALA':
                    biala_czarnego += 1
                    continue
                czarna_bialego += 1

with open('zadanie1_1.txt', 'w') as wynik1, open('zadanie1_2.txt', 'w') as wynik2, open('zadanie1_3.txt', 'w') as wynik3:
    wynik1.write(f'{plansza_pusta_kolumna_liczba} {max_puste_kolumny}')
    wynik2.write(f'{plansze_rownowaga} {min_bierki_rownowaga}')
    wynik3.write(f'{biala_czarnego} {czarna_bialego}')