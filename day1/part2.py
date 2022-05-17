class FinalException(BaseException):
    def __init__(self, j=None):
        with open('output2.txt', 'w') as O:
            O.write(str(j))
        print(format(j))

while True:
    try:
        FloorUp = 0
        FloorDown = 0

        with open('input.txt', 'r') as I:
            FloorUp = 0
            FloorDown = 0
            k = 0
            for i in I:
                for j in range(len(i)):
                    k += 1
                    if i[j] == '(':
                        FloorUp += 1
                    elif i[j] == ')':
                        FloorDown += 1
                        if (FloorUp - FloorDown) == -1:
                            raise FinalException(k)
                    else:
                        raise ZeroDivisionError

        j = 0
        for i in text:
            j += 1
            if i == '(':
                FloorUp += 1
            elif i == ')':
                FloorDown += 1
                if FloorUp - FloorDown == -1:
                    raise FinalException(j)
            else:
                raise ZeroDivisionError
    except FinalException:
        break
