f = open("input.txt", 'rt')

res = 0


def repeat(string):
    for i in range(len(string) - 3):
        pair = string[i:i+2]

        if pair in string[i+2:]:
            return True

    return False


def divided(string):
    for i in range(len(string) - 2):
        if string[i] == string[i+2]:
            return True

    return False


def nice(string):
    return repeat(string) and divided(string)


for line in f:
    if nice(line):
        res += 1

print(res)

o = open('output2.txt', 'w')
o.write(str(res))
o.close()