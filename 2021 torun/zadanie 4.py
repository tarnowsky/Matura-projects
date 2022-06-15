wyniki1 = open('wyniki_znajomi_1.txt', 'w')
wyniki2 = open('wyniki_znajomi_2.txt', 'w')

file1 = open('znajomi_1.txt', 'r')
file2 = open('znajomi_2.txt', 'r')

wiersze1 = file1.readlines()
wiersze2 = file2.readlines()

znajomi_1 = [[int(x) for x in i.strip().split(' ')[1:]] for i in wiersze1[1:]]
znajomi_2 = [[int(x) for x in i.strip().split(' ')[1:]] for i in wiersze2[1:]]

znajomi_1_dict = {i: znajomi_1[i] for i in range(len(znajomi_1))}
znajomi_2_dict = {i: znajomi_2[i] for i in range(len(znajomi_2))}

#zadanie 4.2
def nieznane_osoby(dict):
    znajomosci = {i: 0 for i in  range(len(dict))}
    for osoba, znajomi in dict.items():
        for znajomy in znajomi:
            znajomosci[znajomy] += 1
    lonely = [list(znajomosci.keys())[i] for i in range(len(dict)) if list(znajomosci.values())[i] == 0]
    if len(lonely) == 0:
        return -1
    return lonely

# print(nieznane_osoby(znajomi_1_dict), nieznane_osoby(znajomi_2_dict))
wyniki1.write(f'ZADANIE 4.2\n')
for i in nieznane_osoby(znajomi_1_dict):
    wyniki1.write(f'{i} ')

wyniki2.write(f'ZADANIE 4.2\n')
for i in nieznane_osoby(znajomi_2_dict):
    wyniki2.write(f'{i} ')

#zadanie 4.3
def pary_znajomych(dict):
    pary = []
    index = 0
    for osoba, znajomi in dict.items():
        for i in range(index):
            if list(dict.keys())[i] in znajomi and osoba in list(dict.values())[i]:
                pary.append((osoba, list(dict.keys())[i]))
        index += 1
    return pary

# print(pary_znajomych(znajomi_1_dict))
# print(pary_znajomych(znajomi_2_dict))
wyniki1.write('\n\nZADANIE 4.3\n')
for x, y in pary_znajomych(znajomi_1_dict):
    wyniki1.write(f'{x} {y}\n')

wyniki2.write('\n\nZADANIE 4.3\n')
for x, y in pary_znajomych(znajomi_2_dict):
    wyniki2.write(f'{x} {y}\n')

