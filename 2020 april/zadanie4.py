wyniki = open('zadanie4.txt', 'w')

file = open('dane4.txt', 'r')
wiersze = file.readlines()
liczby = [int(num.strip()) for num in wiersze]
# liczby = [4,11,4,1,4,7,11,12,13,14,7,0,3]
def luka(a, b):
    return abs(a-b)

luki = [abs(liczby[i]-liczby[i+1]) for i in range(len(liczby)-1)]
# print(luki)
#zadanie 4.1
wyniki.write(f'ZADANIE 4.1\nmax luka {max(luki)}\nmin luka {min(luki)}')

#zadanie 4.2

wyniki.write(f'\n\nZADANIE 4.2\n')
max_dl = 0
max_poczatek_ciagu = ''
max_koniec_ciagu = ''
for i in range(len(liczby)-1):
    dl_ciagu = 2
    poczatek_ciagu = liczby[i]
    aktualna_luka = luka(liczby[i], liczby[i+1])
    for j in range(i,len(liczby)-2):
        if luka(liczby[j+1], liczby[j+2]) == aktualna_luka:
            dl_ciagu += 1
        if dl_ciagu >= max_dl:
            max_dl = dl_ciagu
            # max_poczatek_ciagu = poczatek_ciagu
            # max_koniec_ciagu = liczby[j+1]
        if luka(liczby[j + 1], liczby[j + 2]) != aktualna_luka:
            break

for i in range(len(liczby)-1):
    dl_ciagu = 2
    poczatek_ciagu = liczby[i]
    aktualna_luka = luka(liczby[i], liczby[i+1])
    for j in range(i,len(liczby)-2):
        if luka(liczby[j+1], liczby[j+2]) == aktualna_luka:
            dl_ciagu += 1
        if dl_ciagu == max_dl:
            koniec_ciagu = liczby[j+2]
            # print(poczatek_ciagu, dl_ciagu, koniec_ciagu)
            wyniki.write(f'{poczatek_ciagu} {dl_ciagu} {koniec_ciagu}\n')
            break
        if luka(liczby[j + 1], liczby[j + 2]) != aktualna_luka:
            break

#zadanie 3
wyniki.write('\nZADANIE 4.3\n')
dict_luk = {l: luki.count(l) for l in set(luki)}
# print(dict_luk)
max_luka_wystapienia = max(list(dict_luk.values()))
wyniki.write(f'ilosc wystapien luki: {max_luka_wystapienia}\n')
for k, v in zip(dict_luk.keys(), dict_luk.values()):
    if v == max_luka_wystapienia:
        wyniki.write(f'luka: {k}\n')
