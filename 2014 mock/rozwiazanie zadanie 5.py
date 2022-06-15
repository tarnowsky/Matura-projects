with open('dziennik.txt', 'r') as dziennik:
    dziennik = dziennik.readlines()
    dziennik = [int(rek.strip()) for rek in dziennik]

class Rozwiazanie():
    def __init__(self, dziennik):
        self.dziennik = dziennik

    def zadanie_5_1(self):
        serie_wieksze_niz_3 = 0
        dziennik = self.dziennik
        dl_serii = 1
        czy_seria_dluzsza_od_3 = False
        for i in range(len(dziennik)-1):
            aktualny_rek = dziennik[i]
            nastepny_rek = dziennik[i+1]
            if aktualny_rek < nastepny_rek:
                dl_serii += 1
            if dl_serii > 3 and not czy_seria_dluzsza_od_3:
                serie_wieksze_niz_3 += 1
                czy_seria_dluzsza_od_3 = True
            if aktualny_rek >= nastepny_rek:
                dl_serii = 1
                czy_seria_dluzsza_od_3 = False
        return serie_wieksze_niz_3

    def zadanie_5_2(self):
        dziennik = self.dziennik
        maksymalny_wynik = max(dziennik)
        minimalny_wynik = min(dziennik)
        ktory_max = ktory_min = 1
        ktory_max += dziennik.index(maksymalny_wynik)
        ktory_min += dziennik.index(minimalny_wynik)
        return maksymalny_wynik, ktory_max, minimalny_wynik, ktory_min

    def zadanie_5_3(self):
        maks_seria = 0
        aktualna_seria = 1
        dziennik = self.dziennik
        poczatek = dziennik[0]
        koniec = 0
        maks_poczatek = 0
        maks_koniec = 0
        for i in range(len(dziennik)-1):
            aktualny_rek = dziennik[i]
            nastepny_rek = dziennik[i+1]
            if aktualny_rek < nastepny_rek:
                aktualna_seria += 1
                koniec = nastepny_rek
            if aktualna_seria > maks_seria:
                maks_seria = aktualna_seria
                maks_poczatek = poczatek
                maks_koniec = koniec
            if aktualny_rek >= nastepny_rek:
                poczatek = nastepny_rek
                aktualna_seria = 1
        return maks_seria, maks_koniec - maks_poczatek

r = Rozwiazanie(dziennik)

with open('wyniki5.txt', 'w') as wyniki:
    wyniki.write(f'ZADANIE 5.1.\n'
                 f'{r.zadanie_5_1()}\n\n')
    wynik2 = r.zadanie_5_2()
    wyniki.write(f'ZADANIE 5.2.\n'
                 f'maks wynik, ktory z kolei: {wynik2[0], wynik2[1]}\n'
                 f'min wynik, ktory z kolei: {wynik2[2], wynik2[3]}\n\n')
    wynik3 = r.zadanie_5_3()
    wyniki.write(f'ZADANIE 5.3.\n'
                 f'maks seria: {wynik3[0]}\n'
                 f'poprawa wyniku: {wynik3[1]}cm')
