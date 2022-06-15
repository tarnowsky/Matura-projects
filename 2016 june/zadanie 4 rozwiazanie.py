with open('liczby.txt', 'r') as file:
    wiersze = file.readlines()
    systemy_liczbowe_tab = [wiersz.strip() for wiersz in wiersze]

wyniki1 = open('wyniki_6_1.txt', 'w')
wyniki2 = open('wyniki_6_2.txt', 'w')
wyniki3 = open('wyniki_6_3.txt', 'w')
wyniki4 = open('wyniki_6_4.txt', 'w')
wyniki5 = open('wyniki_6_5.txt', 'w')

class SystemyLiczbowe():
    def __init__(self, tab):
        self.systemy_liczbowe_tab = tab

    def zadanie_6_1(self):
        ile_w_systemie_osemkowym = 0
        for ciag in self.systemy_liczbowe_tab:
            system_liczbowy = ciag[-1]
            if system_liczbowy == '8':
                ile_w_systemie_osemkowym += 1
        return ile_w_systemie_osemkowym

    def zadanie_6_2(self):
        ile_w_systemie_czworkowym_bez_0 = 0
        for ciag in self.systemy_liczbowe_tab:
            system_liczbowy = ciag[-1]
            if system_liczbowy == '4' and '0' not in ciag:
                ile_w_systemie_czworkowym_bez_0 += 1
        return ile_w_systemie_czworkowym_bez_0

    def zadanie_6_3(self):
        ile_parzyste_w_dwojkowym = 0
        for ciag in self.systemy_liczbowe_tab:
            system_liczbowy = ciag[-1]
            liczba = ciag[:len(ciag) - 1]
            if system_liczbowy == '2':
                if int(liczba, 2) % 2 == 0:
                    ile_parzyste_w_dwojkowym += 1
        return ile_parzyste_w_dwojkowym

    def zadanie_6_4(self):
        suma_liczb_w_systemie_osemkowym = 0
        for ciag in self.systemy_liczbowe_tab:
            system_liczbowy = ciag[-1]
            if system_liczbowy == '8':
                suma_liczb_w_systemie_osemkowym += int(ciag[:len(ciag) - 1], 8)
        return suma_liczb_w_systemie_osemkowym

    def zadanie_6_5(self):
        max_liczba_10 = 0
        max_liczba_sys = 0
        min_liczba_10 = 100_000_000
        min_liczba_sys = 999_999_999
        for ciag in self.systemy_liczbowe_tab:
            system_liczbowy = int(ciag[-1])
            liczba = ciag[:len(ciag) - 1]
            liczba_10 = int(liczba, system_liczbowy)
            max_liczba_10 = max(max_liczba_10, liczba_10)
            min_liczba_10 = min(min_liczba_10, liczba_10)
            if max_liczba_10 == liczba_10:
                max_liczba_sys = ciag
            if min_liczba_10 == liczba_10:
                min_liczba_sys = ciag
        return max_liczba_10, max_liczba_sys, min_liczba_10, min_liczba_sys

rozwiazanie = SystemyLiczbowe(systemy_liczbowe_tab)
if __name__ == "__main__":
    wyniki1.write(f'{rozwiazanie.zadanie_6_1()}')
    wyniki2.write(f'{rozwiazanie.zadanie_6_2()}')
    wyniki3.write(f'{rozwiazanie.zadanie_6_3()}')
    wyniki4.write(f'{rozwiazanie.zadanie_6_4()}')
    wyniki5.write(f'największa liczba w systemie dziesiętnym: {rozwiazanie.zadanie_6_5()[0]}\n'
                  f'kod liczby: {rozwiazanie.zadanie_6_5()[1]}\n'
                  f'najmniejsza liczba w systemie dziesiętnym: {rozwiazanie.zadanie_6_5()[2]}\n'
                  f'kod liczby: {rozwiazanie.zadanie_6_5()[3]}')