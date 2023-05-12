def z1():
    try:
        number = int(input('Введите число: '))
    except ValueError:
        print('Это не число!')
    else:
        if number % 3 == 0:
            print(f"{number} делится на 3!")
        elif number == 0:
            print('Введён 0!')
        else:
            print(f"{number} не делится на 3!")
def z2():
    try:
        n = int(input('Введите число: '))
        v = 100 / n
    except ValueError:
        print('Это не число!')
    except ZeroDivisionError:
        print('Введён 0!')
    else:
        print(f'100 : {n} = {v}')
def z3():
    d = input('Введите дату: ')
    d = d.split('.')
    if int(d[0]) * int(d[1]) == int(d[2][2 : 4]):
        print('Дата магическая!')
    else:
        print('Увы, дата не магическая :(')
def z4():
    n = input('Введите номер билета: ')
    a = 0
    b = 0
    if len(n) % 2 == 0:
        for i in n[0:int(len(n) / 2)]:
            a = a + int(i)
        for i in n[int(len(n) / 2):int(len(n)) + 1]:
            b = b + int(i)
        if a == b:
            print('Билет счастливый!')
        else:
            print('Билет не счастливый :(')
    else:
        print('Нечётное количество цифр!')
