f = open("input.txt", 'rt')

res = 0


def gl(string):
    gls = [char for char in string if char in ['a', 'e', 'i', 'o', 'u']]

    return len(gls) >= 3


def repeat(string):
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            return True

    return False


def blacklist(string):
    for blacklisted in ['ab', 'cd', 'pq', 'xy']:
        if blacklisted in string:
            return False

    return True


def nice(string):
    return gl(string) and repeat(string) and blacklist(string)


for line in f:
    if nice(line):
        res += 1

print(res)

o = open('output1.txt', 'w')
o.write(str(res))
o.close()
