f = open('input.txt', 'rt')

instr = f.read()
i = 0

s_x = 0
s_y = 0
r_x = 0
r_y = 0

crd = ['0,0']

while i < len(instr):
    if instr[i] == '>':
        if i % 2 == 0:
            s_x += 1
        else:
            r_x += 1
    if instr[i] == '<':
        if i % 2 == 0:
            s_x -= 1
        else:
            r_x -= 1
    if instr[i] == 'v':
        if i % 2 == 0:
            s_y -= 1
        else:
            r_y -= 1
    if instr[i] == '^':
        if i % 2 == 0:
            s_y += 1
        else:
            r_y += 1

    if i % 2 == 0:
        crd.append(str(s_x) + ',' + str(s_y))
    else:
        crd.append(str(r_x) + ',' + str(r_y))

    i += 1

print(crd)
a = len(set(crd))
print(a)

o = open('output2.txt', 'w')
o.write(str(len(set(crd))))
o.close()
