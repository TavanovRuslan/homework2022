import re
s = open("input.txt", "r")
s = s.read()

a = re.compile(r'((\d)\2*)')


def replace(match_obj):
    s = match_obj.group(1)
    return str(len(s)) + s[0]


for i in range(50):
    s = a.sub(replace, s)

out = open("output2.txt", "w")
out.write(str(len(s)))
out.close()
