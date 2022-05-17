class FinalException(BaseException):
    def __init__(self, j=None):
        with open('output1.txt', 'w') as O:
            O.write(str(j))
        print(format(j))


while True:
    try:
        FloorUp = 0
        FloorDown = 0

        with open('input.txt', 'r') as INPUT:
            text = INPUT.readlines()
            text = ''.join(text)

        FloorUp = text.count('(')
        FloorDown = text.count(')')
        raise FinalException(FloorUp - FloorDown)
    except FinalException:
        break
