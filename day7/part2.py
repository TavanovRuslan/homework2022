print('Бобу нужна помощь с проводами и расчётами... Давайте поможем!\n')

array = []


# Функция прохода по проводам
def score(start_element, array):
    letter_dict = {x[1]: x[0] for x in start_element}
    for i in range(len(array)):
        for element in array:

            if element[1] == 'RSHIFT' and element[0] in letter_dict.keys():
                values = int(letter_dict.get(element[0])) >> int(element[2])
                letter_dict.update({element[-1]: values})

            elif element[1] == 'LSHIFT' and element[0] in letter_dict.keys():
                values = int(letter_dict.get(element[0])) << int(element[2])
                letter_dict.update({element[-1]: values})

            elif element[1] == 'NOT' and element[0] in letter_dict.keys():
                values = ~int(letter_dict.get(element[0]))
                letter_dict.update({element[-1]: values})

            elif element[1] == 'OR':
                if element[0] in letter_dict.keys() and element[2] in letter_dict.keys():
                    values = int(letter_dict.get(element[0])) | int(letter_dict.get(element[2]))
                    letter_dict.update({element[-1]: values})
                elif element[0].isdigit() and element[2] in letter_dict.keys():
                    values = int(element[0]) | int(letter_dict.get(element[2]))
                    letter_dict.update({element[-1]: values})
                elif element[0] in letter_dict.keys() and element[2].isdigit():
                    values = int(letter_dict.get(element[0])) | int(element[2])
                    letter_dict.update({element[-1]: values})

            elif element[1] == 'AND':
                if element[0] in letter_dict.keys() and element[2] in letter_dict.keys():
                    values = int(letter_dict.get(element[0])) & int(letter_dict.get(element[2]))
                    letter_dict.update({element[-1]: values})
                elif element[0].isdigit() and element[2] in letter_dict.keys():
                    values = int(element[0]) & int(letter_dict.get(element[2]))
                    letter_dict.update({element[-1]: values})
                elif element[0] in letter_dict.keys() and element[2].isdigit():
                    values = int(letter_dict.get(element[0])) & int(element[2])
                    letter_dict.update({element[-1]: values})
            elif len(element) == 2 and element[0].isalpha() and element[0] in letter_dict.keys():
                values = int(letter_dict.get(element[0]))
                letter_dict.update({element[1]: values})
    print(letter_dict)
    return letter_dict.get('a')


# Преобразуем строки в нужный вид
with open('input.txt', 'r') as INPUT:
    for line in INPUT:
        line = line.strip()
        line = line.split()
        line.remove('->')
        array.append(line)

# Ищем начальный элемент и смещаем "NOT" на одну позицию справа
start_element = []
for element in array:
    if element[0].isdigit() and len(element) == 2:
        if element[1] == 'b':
            start_element.insert(0, element)
        else:
            start_element.append(element)

    if element[0] == 'NOT':
        element[0] = element[1]
        element[1] = 'NOT'

# Первый расчёт
a = score(start_element, array)

# Второй расчёт
start_element[0][0] = str(a)
a = score(start_element, array)

with open('output2.txt', 'w') as OUTPUT:
    OUTPUT.write(str(a))
print('В итоге Боб получит число: ', str(a))