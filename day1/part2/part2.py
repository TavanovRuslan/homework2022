f = open('input.txt', 'rt')

floor = 0

instr = f.read()
i = 0
enter = []
while i < len(instr):
    if instr[i] == '(':
        floor += 1
    if instr[i] == ')':
        floor -= 1

    if floor == -1:
        k = i + 1
        enter.append(k)

    i += 1

print('floor =', floor)
print('enter to basement =', min(enter))


