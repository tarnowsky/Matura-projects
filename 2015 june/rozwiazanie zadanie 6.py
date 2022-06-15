with open('kody.txt', 'r') as kody, open('cyfra_kodkreskowy.txt', 'r') as cyfra_kod:
    wiersze = kody.readlines()
    kody = [wiersz.strip() for wiersz in wiersze]
    wiersze = cyfra_kod.readlines()
    cyfra_kod = {wiersz.strip().split('\t')[0]: wiersz.strip().split('\t')[1] for wiersz in wiersze[1:]}

START = '11011010'
STOP = '11010110'
def suma_p_np(a:str):
    suma_p = 0
    suma_np = 0
    for i, num in enumerate(a[::-1]):
        if i % 2 == 0:
            suma_p += int(num)
        else:
            suma_np += int(num)
    return suma_p, suma_np

def cyfra_kontrolna(a:str):
    suma_p, suma_np = suma_p_np(a)
    suma_3p_np = suma_p*3 + suma_np
    wynik = (10 - (suma_3p_np % 10)) % 10
    return wynik

def Standard_Code_25(a:str, cyfra_kontr=False):
    wynik = ''
    if cyfra_kontr == False:
        wynik += START
    for num in a:
        wynik += ' ' + cyfra_kod[num]
    if cyfra_kontr == False:
        wynik += Standard_Code_25(str(cyfra_kontrolna(a)), True)
        wynik += ' ' + STOP
    return wynik

with open('kody1.txt', 'w') as kody1, open('kody2.txt', 'w') as kody2, open('kody3.txt', 'w') as kody3:
    for liczba in kody:
        suma_p, suma_np  = suma_p_np(liczba)
        kody1.write(f'{suma_p} {suma_np}\n')
        cyfra_kontr = cyfra_kontrolna(liczba)
        kod_cyfry_kontrolnej = Standard_Code_25(str(cyfra_kontr), True)
        kody2.write(f'{cyfra_kontr} {kod_cyfry_kontrolnej}\n')
        kod = Standard_Code_25(liczba)
        kody3.write(f'{kod}\n')


