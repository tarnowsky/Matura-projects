file = open('NAPIS.TXT', 'r')
file = file.readlines()
napisy = [napis.strip() for napis in file]

wyniki = open('wyniki.txt', 'w')

# a)
def pierwsza(a):
    if a == 2:
        return True
    if a < 2 or a % 2 == 0:
        return False
    for n in range(3, int(a**0.5)+1, 2):
        if a % n == 0:
            return False
    return True

ile_pierwszych = 0
for napis in napisy:
    suma_asci = 0
    for litera in napis:
        suma_asci += ord(litera)
    if pierwsza(suma_asci):
        ile_pierwszych += 1
wyniki.write(f'a) {ile_pierwszych}\n')

# b)
wyniki.write('b)\n')
for napis in napisy:
    for i in range(len(napis)-1):
        if napis[i] >= napis[i+1]:
            break
    else: wyniki.write(f'{napis}\n')

# c)
wyniki.write('c)\n')
dict_napisow = {napis: napisy.count(napis) for napis in set(napisy)}
for k,v in dict_napisow.items():
    if v > 1:
        wyniki.write(f'{k}\n')
