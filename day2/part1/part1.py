# 2*l*w + 2*w*h + 2*h*l
f = open("input.txt", 'rt')

instr = []

for line in f:
    instr.append(line)

i = 0
result = 0

while i < len(instr):
    a = instr[i].split('x')

    a[0] = int(a[0])
    a[1] = int(a[1])
    a[2] = int(a[2])

    res = (2 * a[0] * a[1]) + (2 * a[1] * a[2]) + (2 * a[0] * a[2])
    moa = min(a[0] * a[1], a[1] * a[2], a[2] * a[0])
    print(res)
    result += res + moa

    i += 1

print('result = ', result)

o = open('output1.txt', 'w')
o.write(str(result))
o.close()