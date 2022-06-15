with open('Dane2018/ciagi.txt', 'r') as file:
    ciagi = file.readlines()
    ciagi_tab = [[int(i) for i in ciag.strip().split(' ')[1:]] for ciag in ciagi[1:]]

def PodciągRosnący(lista):
  lista_rosnąca=[1 for i in range(len(lista))]
  for i in range(len(lista)):
    for j in range(i,-1,-1):
      if lista[j] < lista[i] and lista_rosnąca[j] >= lista_rosnąca[i]:
        lista_rosnąca[i]=lista_rosnąca[j]+1
        print(j, i, lista[j], lista[i], lista_rosnąca)
  k=max(lista_rosnąca)
  return k


print(PodciągRosnący([12,9,13,10,11,14,15,12]))
