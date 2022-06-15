wynik1 = open('wyniki4_1.txt', 'w')
wynik2 = open('wyniki4_2.txt', 'w')
wynik3 = open('wyniki4_3.txt', 'w')

with open('identyfikator.txt') as file:
# with open('identyfikator_przyklad.txt') as file:
    max_id_number_sum = 0
    result_1= []
    result_2 = []
    result_3 = []
    dict_letter_number = {chr(i): i-55 for i in range(65,91)}
    wage = [7,3,1,7,3,1,7,3]
    for line in file:
        id = line.strip()
        id_serie = id[:3]
        id_number = id[3:]

        #excercise 1
        id_number_sum = 0
        for i in id_number:
            id_number_sum += int(i)
        if id_number_sum >= max_id_number_sum:
            if id_number_sum > max_id_number_sum:
                result_1.clear()
            max_id_number_sum = id_number_sum
            result_1.append(id)

        #excercise 2
        if id_number == id_number[::-1] or id_serie == id_serie[::-1]:
            result_2.append(id)
            wynik2.write(f'{id}\n')

        #excercise 3
        id_control_number = int(id_number[0])
        id_number = id_number[1:]
        id_control_sum = 0
        for i in range(len(id_serie+id_number)):
            if i < 3:
                id_control_sum += dict_letter_number[id_serie[i]]*wage[i]
            else:
                id_control_sum += int(id_number[i-3])*wage[i]
        id_control_sum %= 10
        if id_control_number != id_control_sum:
            result_3.append(id)
            wynik3.write(f'{id}\n')

    for result in result_1:
        wynik1.write(f'{result}\n')






