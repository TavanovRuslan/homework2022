f = open('input.txt', 'rt')

floor = 0

instr = f.read()
i = 0
while i < len(instr):
    if instr[i] == '(':
        floor += 1
    if instr[i] == ')':
        floor -= 1
    i += 1

print('floor =', floor)

