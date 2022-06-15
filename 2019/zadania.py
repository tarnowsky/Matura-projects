wyniki = open('wyniki4.txt', 'w')

with open('liczby.txt', 'r') as file:
# with open('przyklad.txt', 'r') as file:
    wiersze = file.readlines()
    liczby = [int(wiersz.strip()) for wiersz in wiersze]

#zadanie 1
tab_pot_3 = [3**i for i in range(11)]
ile_pot_3 = 0
for liczba in liczby:
    if liczba in tab_pot_3:
        ile_pot_3 += 1
# print(ile_pot_3)
wyniki.write(f'ZADANIE 1\nile poteg 3: {ile_pot_3}\n\n')

#zadanie 2
def silnia(num):
    if num == 0:
        return 1
    pom = num-1
    while pom > 0:
        num = num*pom
        pom -= 1
    return num

wyniki.write('ZADANIE 2\n')
for liczba in liczby:
    sum = 0
    for cyfra in str(liczba):
        sum += silnia(int(cyfra))
    if sum == liczba:
        wyniki.write(f'{liczba}\n')
        # print(liczba)

#zadanie 3
def nwd(a,b):
    if b == 0:
        return a
    return nwd(b, a%b)

i = 0
aktualna_dlugosc_ciagu = 1
max_dlugosc_ciagu = 0
while i < len(liczby)-2:
    # print(i)
    pierwsza = liczby[i]
    druga = liczby[i+1]
    aktualne_nwd = nwd(pierwsza, druga)
    for index in range(i+2, len(liczby)): #2 bo porownujemy nwd liczby oddalonej o 3 od poczatku
        if nwd(aktualne_nwd, liczby[index]) > 1:
            aktualna_dlugosc_ciagu += 1
        # print(aktualna_dlugosc_ciagu)
        if aktualna_dlugosc_ciagu > max_dlugosc_ciagu:
            max_dlugosc_ciagu = aktualna_dlugosc_ciagu
            max_poczatek_ciagu = pierwsza
            max_nwd = nwd(aktualne_nwd, liczby[index])
        if nwd(aktualne_nwd, liczby[index]) == 1:
            aktualna_dlugosc_ciagu = 2
            i = index #jesli liczby maja nwd == 1 to nie musimy ich pary juz brac pod uwage
            break
# print(max_poczatek_ciagu, max_dlugosc_ciagu, max_nwd)
wyniki.write(f'\nZADANIE 3\npoczatek: {max_poczatek_ciagu}\ndługość: {max_dlugosc_ciagu}\nnwd: {max_nwd}')
# print(nwd(14,91))



