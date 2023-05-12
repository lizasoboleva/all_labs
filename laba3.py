slova = []

while (sl2 := str(input())) != "stop":
    slova.append(sl2)
print(' '.join(slova))
def n1():
    print(" ".join([input('Введите слово: ') for i in range(int(input('Введите количество слов: ')))]))
def n3():
    slova = ('Введите слово: ')
    while (sl2 := str(input())) != "stop":
        if 'ф' in sl2 or 'Ф' in sl2:
            print('Ого! Это редкое слово!')
        else:
            print('Эх, это не очень редкое слово...')
def n4():
    from random import randint

    print('Для завершения игры введите слово stop!')
    while True:
        a = randint(1,100)
        b = randint(1,100)
        print(f"{a} + {b} = ", end='')
        rez = input()
        while not rez.isdigit() and rez != 'stop':
            print('Ошибка, повторите ввод: ', end='')
            rez = input()
        if rez == 'stop':
            break
        rez = int(rez)
        if a+b == rez:
            print('Верно!')
        else:
            print('Ответ неправильный! :(')
