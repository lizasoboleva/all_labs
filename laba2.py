def n1():
    a = input('Введите первый цвет - ')
    b = input('Введите второй цвет - ')

    if a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный':
        print('Цвет после смешивания - фиолетовый')
    elif a == 'красный' and b == 'желтый' or a == 'желтый' and b == 'красный':
        print('Цвет после смешивания - оранжевый')
    elif a == 'синий' and b == 'желтый' or a == 'желтый' and b == 'синий':
        print('Цвет после смешивания - зеленый')
    elif a == 'красный' and b == 'красный':
        print('Цвет после смешивания - красный')
    elif a == 'желтый' and b == 'желтый':
        print('Цвет после смешивания - желтый')
    elif a == 'синий' and b == 'синий':
        print('Цвет после смешивания - синий')
    else:
        print('Ошибка!')

def n2():
    n = int(input("Введите номер места в плацкартном вагоне: "))
    print()

    if n % 2 == 0 and n <= 36:
        print('Ваше место - верхнее, купе.')
    elif n % 2 != 0 and n <= 35:
        print('Ваше место - нижнее, купе.')
    elif n % 2 == 0 and n > 36:
        print('Ваше место - верхнее, боковое.')
    else:
        print('Ваше место - нижнее, боковое.')

def n3():
    pas1 = input("Введите пароль: ")
    pas2 = input("Введите пароль повторно: ")

    if pas1 == pas2:
        print("Пароли совпадают!")
    else:
        print("Пароль не принят.")

def n4():
    # print(' '.join([input()]))
    print(' '.join([input('Введите слово: ') for i in range(int(input('Введите количество слов: ')))]))

def n5():
    n = int(input('Введите год: '))

    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        print(n, 'год - високосный.')
    else:
        print('Этот год не високосный.')

n1(), n2(), n3(), n4(), n5()
