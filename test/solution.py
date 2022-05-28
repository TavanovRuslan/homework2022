from re import split as spliter

#Берем данные из input.txt
with open('input.txt', 'r') as INPUT:
    m = int(INPUT.readline())
    array = []
    for i in range(m):
        array.append(INPUT.readline().strip())


#Избавимся от дубликатов IP-адресов
SET = set()
for el in array:
    SET.add(el)
array = list(SET)


#Представим каждый IP-адрес в битовом формате
bit_array = []
for el in array:
    ar = el.split('.')
    full_string = str()
    for i in ar:
        string = bin(int(i))
        string = string[2:]
        if len(string) < 8:
            string = (8 - len(string))*'0' + string
        full_string += string
    bit_array.append(full_string)


#Определим параметр N
    for i in range(1,33):
        if 2**(i-1) < len(SET) and 2**i >= len(SET):
            n = i
            break


#Определим маску
bit_mask = (32 - n)*'1' + n*'0'
mask = str()
for i in range(4):
    if bit_mask[i*8] != '0':
        mask += str(int('0b' + bit_mask[i*8:(1+i)*8], base=2)) + '.'
    elif bit_mask[i*8:(1+i)*8] == '00000000':
        mask += '0.'
    else:
        print(bit_mask[i*8:(1+i)*8])
        print(spliter('^0+', bit_mask[i*8:(1+i)*8])[-1])
        mask += str(int('0b' + spliter('^0+', bit_mask[i*8:(1+i)*8])[-1], base = 2)) + '.'   #Если больше 256 IP-адресов
mask = mask[:-1]


#Определим IP-сеть
##Создадим новый массив для нахождения наибольшего IP-адрес
new_array = []
for el in array:
    new_array.append([int(x) for x in el.split('.')])
##Ищем наибольший IP-адрес
Max_IP = str()
new_array.sort()
for numb in new_array[-1]:
    Max_IP += str(numb) + '.'
Max_IP = Max_IP[:-1]
##Вычисляем наименьший сетевой адрес
counter = 0
reverse_IP = new_array[-1].copy()
reverse_IP.reverse()
for i in reverse_IP:
    counter += 1
    if i >= 2**n and counter == 1:
        print(i)
        print(n)
        reverse_IP[0] = i - (2**n - 1)
        break
    elif i < 2**n and counter == 2:
        reverse_IP[1] = i - (2**n - 1)//255
        reverse_IP[0] = reverse_IP[0] - (2**n - 1)%255
        break
##Получаем IP-сеть
IP = reverse_IP
IP.reverse()
IP = [str(x) for x in IP]
IP = '.'.join(IP)

    
#Проверяем кода
print('IP-адреса: ', array)
print('IP-адреса в битах: ', bit_array)
print('Наибольшний IP-адрес: ', Max_IP)
print('Маска: ', mask)
print('Сетевой адрес: ', IP)


#Выводим в output.txt
with open('output.txt', 'w') as OUTPUT:
    OUTPUT.write(IP + '\n')
    OUTPUT.write(mask)

