f = open('input.txt', 'rt')

s1 = 0
s2 = 1
instr = []

for line in f:
    trimmed_line = line[:-1]

    escaped_quotes = trimmed_line.replace("\\", "\\\\")
    escaped_slashes = escaped_quotes.replace("\"", "\\\"")

    s1 += len(trimmed_line)
    s2 += (len(escaped_slashes) + 2)
    instr.append(trimmed_line)

print(str(s2 - s1))

o = open('output2.txt', 'w')
o.write(str(s2 - s1))
o.close()