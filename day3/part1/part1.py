f = open('input.txt', 'rt')

instr = f.read()
i = 0

x = 0
y = 0

crd = ['0,0']

while i < len(instr):
    if instr[i] == '>':
        x += 1
    if instr[i] == '<':
        x -= 1
    if instr[i] == 'v':
        y -= 1
    if instr[i] == '^':
        y += 1

    crd.append(str(x) + ',' + str(y))

    i += 1

print(crd)
a = len(set(crd))
print(a)

o = open('output1.txt', 'w')
o.write(str(len(set(crd))))
o.close()
