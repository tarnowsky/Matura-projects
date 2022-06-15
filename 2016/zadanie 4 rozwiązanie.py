import math
import matplotlib.pyplot as plt


with open('punkty.txt', 'r') as file:
    lines = file.readlines()
    punkty_tab = [punkt.strip().split() for punkt in lines]
    x_tab = [int(punkty_tab[i][0]) for i in range(len(punkty_tab))]
    y_tab = [int(punkty_tab[i][1]) for i in range(len(punkty_tab))]

SRODEK_OKREGU = 200
PROMIEN_OKREGU = 200
POLE_KWADRATU = 400 ** 2
PI = math.pi

class Rozwiazanie():
    def __init__(self, punkty_tab, x_tab, y_tab):
        self.tab_punkty = punkty_tab
        self.tab_x = x_tab
        self.tab_y = y_tab

    def zadanie_4_1(self):
        tab_punkty_brzegowe = []
        ile_wewnatrz = 0
        for x, y in zip(self.tab_x, self.tab_y):
            if self.czy_brzeg(x, y):
                tab_punkty_brzegowe.append((x, y))
            elif self.czy_wnetrze(x, y):
                ile_wewnatrz += 1
        return tab_punkty_brzegowe, ile_wewnatrz

    def czy_brzeg(cls, x, y):
        if (x - SRODEK_OKREGU) ** 2 + (y - SRODEK_OKREGU) ** 2 == PROMIEN_OKREGU ** 2:
            return True
        return False

    def czy_wnetrze(cls, x, y):
        if (x - SRODEK_OKREGU) ** 2 + (y - SRODEK_OKREGU) ** 2 < PROMIEN_OKREGU ** 2:
            return True
        return False

    def zadanie_4_2(self, ilosc_puktow = 10_000):
        punkty_kwadratu = ilosc_puktow
        punkty_kola = 0
        for x, y in zip(self.tab_x[:ilosc_puktow], self.tab_y[:ilosc_puktow]):
            if self.czy_brzeg(x, y) or self.czy_wnetrze(x, y):
                punkty_kola += 1
        pi = (punkty_kola * POLE_KWADRATU) / (ilosc_puktow * (PROMIEN_OKREGU ** 2))
        return pi

    def zadanie_4_3(self):
        tab_plot_x = [str(abs(PI - self.zadanie_4_2(i))) + '\n' for i in range(1,1701)]
        return tab_plot_x


if __name__ == "__main__":
    rozwiazanie = Rozwiazanie(punkty_tab, x_tab, y_tab)
    wyniki = open('wyniki_4.txt', 'w')
    wyniki.write(f'ZADANIE 4.1.\n'
          f'Należące do brzegu: {rozwiazanie.zadanie_4_1()[0]}\n'
          f'Należące do wnętrza: {rozwiazanie.zadanie_4_1()[1]}\n\n')
    wyniki.write(f'ZADANIE 4.2.\n'
          f'pi dla 1000 punktów: {rozwiazanie.zadanie_4_2(1000)}\n'
          f'pi dla 5000 punktów: {rozwiazanie.zadanie_4_2(5000)}\n'
          f'pi dla wszystkch punktów: {rozwiazanie.zadanie_4_2()}\n\n')
    wyniki.write(f'ZADANIE 4.3.\n'
          f'e1000: {round(float(rozwiazanie.zadanie_4_3()[999].strip()), 4)}\n'
          f'e1700: {round(float(rozwiazanie.zadanie_4_3()[-1].strip()), 4)}')
    wyniki.close()
    dane_do_wykresu = open('dane do wykresu.txt', 'w')
    for x in rozwiazanie.zadanie_4_3():
        dane_do_wykresu.write(f'{x}')
    dane_do_wykresu.close()
