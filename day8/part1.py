import re

f = open('input.txt', 'rt')

s1 = 0
s2 = 0
instr = []

for line in f:
    trimmed_line = line[:-1]

    no_line = trimmed_line.replace("\\\\", "P")
    no_quotes = no_line.replace("\\\"", "P")
    no_hex_line = re.sub("\\\\x..", "P", no_quotes)

    s1 += len(trimmed_line)
    s2 += (len(no_hex_line) - 2)
    instr.append(trimmed_line)

print(str(s1 - s2))


o = open('output1.txt', 'w')
o.write(str(s1 - s2))
o.close()