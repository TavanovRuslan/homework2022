import itertools as it

array = []
names = []

with open('input.txt', 'r') as INPUT:
    for line in INPUT:
        line = line.replace('happiness units by sitting next to', '')
        line = line.replace('would', '')
        line = line.replace('.', '')
        line = line.strip()
        if 'gain' in line:
            line = line.replace('gain ', '')
        else:
            line = line.replace('lose ', '-')

        array_smth = line.split()
        array_smth[1] = int(array_smth[1])
        array.append(array_smth)
        if array_smth[0] not in names:
            names.append(array_smth[0])
for name in names:
    array.append(['Me', 0, name])
names.append('Me')

iter_names_list = list(it.permutations(names))

score_array = []
for element in iter_names_list:
    score = 0
    for i in range(len(element)):
        if i == 0:
            for element_array in array:
                if (element[i] == element_array[0]) and (element[i + 1] == element_array[2]):
                    score += element_array[1]
            for element_array in array:
                if (element[i] == element_array[0]) and (element[-1] == element_array[2]):
                    score += element_array[1]
        elif i == len(element) - 1:
            for element_array in array:
                if (element[i] == element_array[0]) and (element[0] == element_array[2]):
                    score += element_array[1]
            for element_array in array:
                if (element[i] == element_array[0]) and (element[i - 1] == element_array[2]):
                    score += element_array[1]
            score_array.append(score)
        else:
            for element_array in array:
                if (element[i] == element_array[0]) and (element[i + 1] == element_array[2]):
                    score += element_array[1]
            for element_array in array:
                if (element[i] == element_array[0]) and (element[i - 1] == element_array[2]):
                    score += element_array[1]

print(max(score_array))

with open('output2.txt', 'w') as OUTPUT:
    OUTPUT.write(str(max(score_array)))