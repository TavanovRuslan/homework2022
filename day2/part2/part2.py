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

    wrap = 2 * min(a[0] + a[1], a[1] + a[2], a[2] + a[0])
    bow = a[0]*a[1]*a[2]
    result += wrap + bow

    i += 1
print('result = ', result)

fw = open('output.txt', 'w')
fw.write(str(result))
