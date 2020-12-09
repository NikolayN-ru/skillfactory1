a = [' '] * 9
d = []
play = True  # играем
s = None


def VivodIgrovovoPolya():
    global a

    print('-' * 13)
    for i in range(0, 9, 3):
        print('|', a[i] + ' | ' + a[i + 1] + ' | ' + a[i + 2], '|')
        print('-' * 13)


def polya():
    global a, d
    d = []
    for i in range(len(a)):
        if a[i] == ' ':
            d.append(i)
    return d


def vin(user, i):
    global a, d, s, play
    if a[0] == a[1] == a[2] == i:
        play = False
    elif a[3] == a[4] == a[5] == i:
        play = False
    elif a[6] == a[6] == a[8] == i:
        play = False
    elif a[0] == a[3] == a[6] == i:
        play = False
    elif a[1] == a[4] == a[7] == i:
        play = False
    elif a[2] == a[5] == a[8] == i:
        play = False
    elif a[0] == a[4] == a[8] == i:
        play = False
    elif a[2] == a[4] == a[6] == i:
        play = False
    if play == False:
        VivodIgrovovoPolya()
        print('выйграл игрок _{}_!'.format(user))
        return play


def vvodnubmer(x, y):
    while x not in y:
        x = int(input('введите корректное поле:'))
    return x


def hod_O(f):
    global a, d, s, play
    polya()
    VivodIgrovovoPolya()
    print('свободные поля под номерами: {0}'.format(d))
    f = int(input('игрок Нолик |O|, введите номер поля:'))
    # проверка на коректность игрового поля
    f = vvodnubmer(f, d)

    a[f] = 'O'
    vin('нолик', i='O')
    if play == False:
        return print('________игра завершена')
    hod_X(s)


def hod_X(f):
    global a, d, s, play
    polya()
    VivodIgrovovoPolya()
    print('свободные поля под номерами: {0}'.format(d))
    f = int(input('игрок Крестик |X|, введите номер поля:'))
    f = vvodnubmer(f, d)

    a[f] = 'X'
    vin('крестик', i='X')
    if play == False:
        return print('________игра завершена')
    hod_O(s)


j = str(input('выберете игрока Нолик -|o| или Крестик -|x|'))
if j == 'o':
    hod_O(s)
elif j == 'x':
    hod_X(s)
else:
    print('некоректно введен игрок')
