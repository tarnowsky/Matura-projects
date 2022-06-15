wyniki = open('wyniki4.txt', 'w')

# file = open('przyklad.txt', 'r')
file = open('sygnaly.txt', 'r')
wiersze = file.readlines()

sygnaly = [wiersz.strip() for wiersz in wiersze]
#zadanie 1
wynik = ''
for i in sygnaly[39::40]:
    wynik += i[9]
# print(wynik)
wyniki.write(f'ZADANIE 1\n{wynik}\n\n')

#zadanie 2
max_ilosc_lit = 0
for sygnal in sygnaly:
    if len(set(sygnal)) > max_ilosc_lit:
        max_ilosc_lit = len(set(sygnal))
        max_sygnal = sygnal
# print(max_sygnal, max_ilosc_lit)
wyniki.write(f'ZADANIE 2\n{max_sygnal} {max_ilosc_lit}\n\n')

#zadanie 3
wyniki.write('ZADANIE 3\n')
for sygnal in sygnaly:
    sygnal_num = [ord(litera) for litera in list(set(sygnal))]
    max_sygnal_num = max(sygnal_num)
    min_sygnal_num = min(sygnal_num)
    odleglosc = max_sygnal_num - min_sygnal_num
    if odleglosc <= 10:
        # print(sygnal)
        wyniki.write(f'{sygnal}\n')