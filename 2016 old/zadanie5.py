with open('gra.txt', 'r') as file:
    lines = file.readlines()
    gra_w_zycie_plansza = [[nod for nod in row.strip()] for row in lines]

class Gra_W_Zycie:
    global gra_w_zycie_plansza
    def __init__(self, plansza):
        self.plansza = plansza

    def zadanie_5_1(self, pokolenie):
        return self.zmiana_pokolen(self.plansza, pokolenie)

    def zadanie_5_2(self, pokolenie):
        zywi = 0
        for row in self.zmiana_pokolen(self.plansza, pokolenie):
            for nod in row:
                if nod == 'X':
                    zywi += 1
        return zywi

    def zadanie_5_3(self):
        for i in range(1, 100):
            aktualna_plansza = self.zadanie_5_1(i)
            nastepna_plansza = self.zadanie_5_1(i + 1)
            if aktualna_plansza == nastepna_plansza:
                return i + 1, self.zadanie_5_2(i + 1)


    def zmiana_pokolen(self, plansza, liczba_symulacji):
        liczba_symulacji -= 1
        if liczba_symulacji == 0:
            return plansza
        nowa_plansza = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                        ]

        for index_row, row in enumerate(plansza):
            for index_nod, nod in enumerate(row):
                zywa = True
                if nod == '.': zywa = False
                zywi_sasiedzi = self.zywi_sasiedzi(index_row, index_nod, plansza)
                if zywa and (zywi_sasiedzi == 2 or zywi_sasiedzi == 3):
                    nowa_plansza[index_row][index_nod] = 'X'
                elif not zywa and zywi_sasiedzi == 3:
                    nowa_plansza[index_row][index_nod] = 'X'
                else: nowa_plansza[index_row][index_nod] = '.'

        return self.zmiana_pokolen(nowa_plansza, liczba_symulacji)

    def zywi_sasiedzi(self, index_row, index_nod, plansza=gra_w_zycie_plansza):
        zywi = 0
        for i in range(-1, 2, 2):
            nowy_index_row = i + index_row
            nowy_index_nod = i + index_nod

            if nowy_index_nod == len(plansza[0]):
                nowy_index_nod = 0
            if nowy_index_row == len(plansza):
                nowy_index_row = 0

            if plansza[nowy_index_row][index_nod] == 'X':
                zywi += 1
            if plansza[index_row][nowy_index_nod] == 'X':
                zywi += 1

            for j in range(-1, 2, 2):
                nowy_index_nod = index_nod + j
                if nowy_index_nod == 20:
                    nowy_index_nod = 0

                if plansza[nowy_index_row][nowy_index_nod] == 'X':
                    zywi += 1
        return zywi

rozwiazanie = Gra_W_Zycie(gra_w_zycie_plansza)

# WYNIKI
wyniki = open('wyniki_5.txt', 'w')
wyniki.write(f'ZADANIE 5.1.\n'
             f'{rozwiazanie.zywi_sasiedzi(1,18,rozwiazanie.zadanie_5_1(37))}\n\n'
             f'ZADANIE 5.2.\n'
             f'{rozwiazanie.zadanie_5_2(2)}\n\n'
             f'ZADANIE 5.3.\n'
             f'{rozwiazanie.zadanie_5_3()}')
