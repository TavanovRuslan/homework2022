from hashlib import md5

f = open('input.txt', 'rt')
key = f.read()

for i in range(9999999):
    h = md5((key + str(i)).encode()).hexdigest()
    if h[:5] == '00000':
        print(h)
        print(i)
        break

o = open('output1.txt', 'w')
o.write(str(i))
o.close()