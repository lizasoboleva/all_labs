def n1():
    s = [1, 2, 3, 4, 5]
    x = int(input('Введите число: '))
    if x in s:
        print('Поздравляю, вы угадали число!')
    else:
        print('Нет такого числа!')
def n2():
    s = [1 ,3 ,4 ,3 ,5 ,4]
    d = {x for x in s if s.count(x)>1}
    print(*d)
def n3():
    days = ('Пн','Вт','Ср','Чт','Пт','Сб','Вс')
    s = int(input('Введите количество выходных: '))
    for i in days:
        print('Ваши рабочие дни: ', *days[:-s])
        print('Ваши выходные дни: ', *days[-s:])
        break
def n4():
    import random
    gr1=('Аа','Ке','Яр','Тр','Зи','Ст','Ка','Ку','Ме','Со')
    gr2 = ('Еп', 'Су', 'Уз', 'Ор', 'Ид', 'Ык', 'Ло', 'Се', 'Зе', 'Юс')
    a1 = []
    a2 = []
    a = []
    a1.append(random.sample(gr1,5))
    a2.append(random.sample(gr1, 5))
    a.extend(*a1)
    a.extend(*a2)
    a = tuple(a)
    print('a', *gr1)
    print('a', *gr2)
    print('a', *a)
    print('b', len(a))
    print('d', *sorted(a))
    print('e', 'Иванов' in a)
    print('e', a.count('Иванов)'))
    
n1(),n2(),n3(),n4()