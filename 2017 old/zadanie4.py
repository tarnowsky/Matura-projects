wyniki = open('zadanie4.txt', 'w')

with open('binarne.txt', 'r') as file:
    binarne_brudne = file.readlines()
    binarne = [ciag.strip() for ciag in binarne_brudne]

class Ciagi_binarne():
    def __init__(self, tablica_ciagow):
        self.binarne = tablica_ciagow

    def zadanie_4_1(self):
        liczba_napisow_dwucyklicznych = 0
        max_n = 0
        najdluzszy_napis_dwucykliczny = ''
        for ciag in self.binarne:
            n = len(ciag)
            if n % 2 != 0:
                continue
            mid = n // 2
            if ciag[:mid] == ciag[mid:]:
                liczba_napisow_dwucyklicznych += 1
                max_n = max(max_n, n)
                if n == max_n:
                    najdluzszy_napis_dwucykliczny = ciag
        return liczba_napisow_dwucyklicznych, najdluzszy_napis_dwucykliczny, max_n

    def zadanie_4_2(self):
        liczba_niepoprawnych_napisow = 0
        min_dlugosc_niepoprawnego_napisu = 100
        for ciag in self.binarne:
            n = len(ciag)
            liczba_fragmentow = n // 4
            mnoznik = 1
            while mnoznik <= liczba_fragmentow:
                fragment = self.bin_na_int(ciag[mnoznik*4 - 4:mnoznik*4])
                if fragment > 9:
                    liczba_niepoprawnych_napisow += 1
                    min_dlugosc_niepoprawnego_napisu = min(min_dlugosc_niepoprawnego_napisu, n)
                    break
                mnoznik += 1
        return liczba_niepoprawnych_napisow, min_dlugosc_niepoprawnego_napisu

    def bin_na_int(self, bin_num):
        return int(bin_num, 2)

    def zadanie_4_3(self):
        max_liczba = 0
        max_liczba_bin = ''
        for ciag in binarne:
            liczba_int = self.bin_na_int(ciag)
            if liczba_int > 65_535:
                continue
            max_liczba = max(max_liczba, liczba_int)
            if liczba_int == max_liczba:
                max_liczba_bin = ciag
        return max_liczba_bin, max_liczba

if __name__ == '__main__':
    rozwiazanie = Ciagi_binarne(binarne)
    wyniki.write('ZADANIE 4.1.\n')
    wyniki.write(f'liczba napisów dwucyklicznych: {rozwiazanie.zadanie_4_1()[0]}\n'
                 f'najdluższy napis: {rozwiazanie.zadanie_4_1()[1]}\n'
                 f'dlugosc tego napisu: {rozwiazanie.zadanie_4_1()[2]}\n\n')
    wyniki.write('ZADNIE 4.2.\n')
    wyniki.write(f'liczba niepoprawnych napisów: {rozwiazanie.zadanie_4_2()[0]}\n'
                 f'najmniejsza długość niepoprawngo napisu: {rozwiazanie.zadanie_4_2()[1]}\n\n')
    wyniki.write('ZADANIE 4.3.\n')
    wyniki.write(f'największa liczba dziesiętnie: {rozwiazanie.zadanie_4_3()[0]}\n'
                 f'największa liczba binarnie: {rozwiazanie.zadanie_4_3()[1]}')
    wyniki.close()






