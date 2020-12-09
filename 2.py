a = [' '] * 9
d = []
play = True  # играем
s = None


def VivodIgrovovoPolya():
    global a
    print(a[0] + '|' + a[1] + '|' + a[2])
    print('-----')
    print(a[3] + '|' + a[4] + '|' + a[5])
    print('-----')
    print(a[6] + '|' + a[7] + '|' + a[8])

    print('*******************')
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


def vin(user):
    global a, d, s, play

    if play == False:
        print('выйграл игрок _{}_!'.format(user))
        return play


def vvodnubmer(x, y):
    while x not in y:
        x = int(input('Нолик, введите корректное поле:'))
    return x


def hod_O(f):
    global a, d, s, play
    polya()
    VivodIgrovovoPolya()
    print('свободные поля под номерами: {0}'.format(d))
    f = int(input('игрок Нолик, введите номер поля:'))
    # проверка на коректность игрового поля
    f=vvodnubmer(f, d)
    vin('нолик')
    a[f] = 'O'
    if play == False:
        return print('________игра завершена')
    hod_X(s)


def hod_X(f):
    global a, d, s, play
    polya()
    VivodIgrovovoPolya()
    print('свободные поля под номерами: {0}'.format(d))
    f = int(input('игрок Крестик, введите номер поля:'))
    f = vvodnubmer(f, d)
    vin('крестик')
    a[f] = 'X'
    if play == False:
        return print('________игра завершена')
    hod_O(s)


j = str(input('выберете игрока Нолик - \'o\' или Крестик - \'x\''))
if j == 'o':
    hod_O(s)
elif j == 'x':
    hod_X(s)
else:
    print('некоректно введен игрок')
