with open('dane_6_1.txt') as file1, open('dane_6_2.txt') as file2, open('dane_6_3.txt') as file3:
    lines = file1.readlines()
    dane1 = [wiersz.strip() for wiersz in lines]
    lines = file2.readlines()
    dane2 = [wiersz.strip().split() for wiersz in lines]
    lines = file3.readlines()
    dane3 = [wiersz.strip().split() for wiersz in lines]

dict_lit_ascii = {chr(i): i for i in range(65, 91)}

class SzyfrCezara():
    def __init__(self, dane):
        self.dane = dane

    def zadanie_6_1(self):
        for slowo in self.dane:
            zaszyfrowane_slowo = ''
            for litera in slowo:
                zaszyfrowane_slowo += self.szyfrator(litera)
            yield zaszyfrowane_slowo

    def szyfrator(cls, litera, klucz=107):
        ascii_lit = dict_lit_ascii[litera]
        klucz = klucz % 26
        nowe_ascii_lit = ascii_lit + klucz
        while nowe_ascii_lit > 90:
            nowe_ascii_lit -= 26
        return chr(nowe_ascii_lit)

    def zadanie_6_2(self):
        for slowo_klucz in self.dane:
            slowo = slowo_klucz[0]
            try: klucz = int(slowo_klucz[1])
            except: klucz = 0
            nowe_slowo = ''
            for litera in slowo:
                nowe_slowo += self.deszyfrator(litera, klucz)
            yield nowe_slowo

    def deszyfrator(cls, litera, klucz):
        ascii_litery = dict_lit_ascii[litera]
        klucz = klucz % 26
        nowe_ascii_litery = ascii_litery - klucz
        while nowe_ascii_litery < 65:
            nowe_ascii_litery += 26
        return chr(nowe_ascii_litery)

    def zadanie_6_3(self):
        for slowo_szyfr in self.dane:
            slowo = slowo_szyfr[0]
            szyfr = slowo_szyfr[1]
            tab_mozliwych_slow = []
            for klucz in range(26):
                nowe_slowo = ''
                for litera in slowo:
                     nowe_slowo += self.szyfrator(litera, klucz)
                tab_mozliwych_slow.append(nowe_slowo)
            if szyfr not in tab_mozliwych_slow:
                yield slowo

rozwiazanie1 = SzyfrCezara(dane1)
rozwiazanie2 = SzyfrCezara(dane2)
rozwiazanie3 = SzyfrCezara(dane3)

wyniki1 = open('wyniki_6_1.txt', 'w')
wyniki2 = open('wyniki_6_2.txt', 'w')
wyniki3 = open('wyniki_6_3.txt', 'w')

for i in rozwiazanie1.zadanie_6_1():
    wyniki1.write(f'{i}\n')
for i in rozwiazanie2.zadanie_6_2():
    wyniki2.write(f'{i}\n')
for i in rozwiazanie3.zadanie_6_3():
    wyniki3.write(f'{i}\n')
