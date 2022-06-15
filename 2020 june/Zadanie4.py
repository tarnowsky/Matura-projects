wyniki = open('wyniki4.txt', 'w')

plik = open('pary.txt', 'r')
# plik = open('przyklad.txt', 'r')
wiersze = plik.readlines()

liczby = [int(num.strip().split(' ')[0]) for num in wiersze]
litery = [string.strip().split(' ')[1] for string in wiersze]

from pprint import pprint
from random import randrange

#zadanie 4.1.
wyniki.write('ZADANIE 4.1.\n')
def czy_piersza(num):
    if num == 2:
        return True
    if num <2 or num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

for num in liczby:
    if num % 2 == 0:
        for i in range(num-1, -1, -1):
            if czy_piersza(i) and czy_piersza(num - i):
                # print(num, num-i, i)
                wyniki.write(f'{num} {num-i} {i}\n')
                break

wyniki.write(f'\nZADANIE 4.2\n')
for slowo in litery:
    max_litera = ''
    max_litera_wystapienia = 0
    aktualna_litera_wystapienia = 1
    for i in range(len(slowo)-1):
        aktualna_litera = slowo[i]
        nastepna_litera = slowo[i+1]

        if aktualna_litera == nastepna_litera:
            aktualna_litera_wystapienia += 1

        if aktualna_litera_wystapienia > max_litera_wystapienia:
            max_litera_wystapienia = aktualna_litera_wystapienia
            max_litera = aktualna_litera

        if aktualna_litera != nastepna_litera:
            aktualna_litera_wystapienia = 1

    # print(max_litera*max_litera_wystapienia, max_litera_wystapienia)
    wyniki.write(f'{max_litera*max_litera_wystapienia} {max_litera_wystapienia}\n')

wyniki.write('\nZADANIE 4.3\n')
min_num = 101
min_slowo = 'z'*50
for num, slowo in zip(liczby, litery):
    if num == len(slowo):
        if num < min_num:
            min_num = num
        if num == min_num:
            if slowo < min_slowo:
                min_slowo = slowo
# print(min_num, min_slowo)
wyniki.write(f'{min_num} {min_slowo}')



