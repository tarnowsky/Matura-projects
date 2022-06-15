file = open('dane.txt', 'r')
wiersze = file.readlines()
liczby_z_pliku = [int(wiersz.strip()) for wiersz in wiersze]

#------------------STARY ALGORYTM------------------
#
# szczesliwa = 1
# nie_szczesliwa = 0
# tab = [szczesliwa for i in range(10_000)]
#
# indeks_poprzedniej_szczesliwej = 0 #piersza liczba szczesliwa to 1
# for i in range(len(tab)):
#     #wyjątek kiedy nie czyscimy tabeli po liczbie szczesliwej, tylko po 2
#     if i == 0:
#         for j in range(1,len(tab),2):
#             tab[j] = nie_szczesliwa
#         indeks_poprzedniej_szczesliwej = 0
#         liczba_szczesliwa = 1
#         # print(liczba_szczesliwa)
#         continue
#
#     liczba_szczesliwa = tab[indeks_poprzedniej_szczesliwej+1:].index(szczesliwa) + indeks_poprzedniej_szczesliwej + 1 + 1
#
#     # print(liczba_szczesliwa)
#     ile_bylo_szczesliwych = 0
#     for j in range(len(tab)):
#         if tab[j] == szczesliwa:
#             ile_bylo_szczesliwych += 1
#         if ile_bylo_szczesliwych == liczba_szczesliwa:
#             tab[j] = nie_szczesliwa
#             ile_bylo_szczesliwych = 0
#     indeks_poprzedniej_szczesliwej = liczba_szczesliwa-1
#
#     if indeks_poprzedniej_szczesliwej == 9998:
#         break
#
# tablica_szczesliwych = [i + 1 for i in range(len(tab)) if tab[i] == 1]
# print(len(tab_wynik))
# print(tab_wynik)
# print(tab_wynik)

#------------------NOWY ALGORYTM------------------

tab_szczesliwych = [[3,2]]
tablica_szczesliwych = [1, 3]

for i in range(5,10_000,2):
    a = False
    for j in range(len(tab_szczesliwych)):
        tab_szczesliwych[j][1] += 1
        a = (tab_szczesliwych[j][1] % tab_szczesliwych[j][0] == 0)
        if a:
            break
    if not a:
        ile_poprzednich_szczesliwych = len(tab_szczesliwych) + 1  # 1 za 1, która jest wyjątkiem
        tab_szczesliwych.append([i, ile_poprzednich_szczesliwych + 1])  # 1 za tą szczesliwą, która właśnie wpadła
        tablica_szczesliwych.append(i)


#------------------ROZWIĄZANIA ZADAŃ------------------

#zadanie 4.1.
szczesliwe_z_pliku = []
wynik = 0
for num in liczby_z_pliku:
    if num in tablica_szczesliwych:
        wynik += 1
        szczesliwe_z_pliku.append(num)
print(wynik)

#zadanie 4.2.
def czy_szczesliwa(liczba):
    if liczba in tablica_szczesliwych:
        return True
    return False

dl_aktualnego_ciagu = 1
pierwsza_liczba_aktualnego_ciagu = szczesliwe_z_pliku[0]
max_dl_ciagu = 0
pierwsza_liczba_max_ciagu = ''

for i in range(len(liczby_z_pliku)-1):
    aktualna_liczba = liczby_z_pliku[i]
    nastepna_liczba = liczby_z_pliku[i+1]

    if not czy_szczesliwa(aktualna_liczba):
        dl_aktualnego_ciagu = 1
        pierwsza_liczba_aktualnego_ciagu = nastepna_liczba

    if czy_szczesliwa(aktualna_liczba) and czy_szczesliwa(nastepna_liczba):
        dl_aktualnego_ciagu += 1

    if dl_aktualnego_ciagu > max_dl_ciagu:
        max_dl_ciagu = dl_aktualnego_ciagu
        pierwsza_liczba_max_ciagu = pierwsza_liczba_aktualnego_ciagu



print(pierwsza_liczba_max_ciagu, max_dl_ciagu)



#zadanie 4.3.
def czy_pierwsza(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

wynik = 0
for num in szczesliwe_z_pliku:
    if czy_pierwsza(num):
        wynik+=1
print(wynik)

