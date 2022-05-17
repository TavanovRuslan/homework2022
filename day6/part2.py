import re

f = open('input.txt', 'rt')


def instruction():
    if 'turn off' in line:
        return lambda x: max(x - 1, 0)
    elif 'toggle' in line:
        return lambda x: x + 2
    elif 'turn on' in line:
        return lambda x: x + 1
    else:
        return lambda x: x


matrix = {}

for i in range(1000):
    for j in range(1000):
        matrix[(i, j)] = 0


for line in f:
    coordinates = re.match("[\D]*(\d+),(\d+)[\D]*(\d+),(\d+)", line)

    apply = instruction()

    for i in range(int(coordinates.group(1)), int(coordinates.group(3)) + 1):
        for j in range(int(coordinates.group(2)), int(coordinates.group(4)) + 1):
            matrix[(i, j)] = apply(matrix[(i, j)])

count = 0

for light in matrix.values():
    count += light

print(count)


o = open('output2.txt', 'w')
o.write(str(count))
o.close()