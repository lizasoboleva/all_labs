def z1():
    import json
    with open('json', 'r', encoding='utf-8') as fl:      #открываем файл только для чтения
        a = json.load(fl)                                #загружаем его
    for i in a['products']:             #в продуктах
        print('Название:', i['name'])    #записываем что к чему относится в коде
        print('Цена:', i['price'])
        print('Вес: ', i['weight'])
        if i['available']:              #если доступно, то выводим в наличии
            print('В наличии')
        else:                           #иначе не в наличии
            print('Нет в наличии')

def z2():
    import json
    with open('json', 'r', encoding='utf-8') as fl:    #снова открываем файл для чтения
        a = json.load(fl)
    for i in a['products']:
        print('Название:', i['name'])
        print('Цена:', i['price'])
        print('Вес: ', i['weight'])
        if i['available']:
            print('В наличии')
        else:
            print('Нет в наличии')
    name = input('Введите название:')     #поля для ввода инфы
    price = input('Введите цену:')
    weight = input('Введите вес:')
    available = input(str('В наличии, введите да или нет:'))
    print('Название:', name)             #выводим соответствующие данные введённым результатам
    print('Цена:', price)
    print('Вес: ', weight)
    print('В наличие или нет: ', available)

def z3():
    a = {}   #словарь
    with open('en-ru.txt', encoding='utf-8') as f:    #открываем словарь слов на англ
        while True:
            line = f.readline()   #возвращает очередную строку файла
            if not line:
                break
            fdata = line.split('-')  #разбивает строку на список строк
            fdata[0] = fdata[0].lstrip().rstrip()  #возвращает копию строки, удаляя как начальные, так и конечные символы
            for j in fdata[1].split(','):
                j = j.lstrip().rstrip()   #короче здесь мы форматируем словарь в файл наоборот
                if j not in a:
                    a[j] = [fdata[0]]
                else:
                    a[j].append(fdata[0])
    sd = dict(sorted(a.items()))     #сортировка по алфавиту
    with open('ru-en.txt', 'w', encoding='utf-8') as f:   #открываем новый файл для редактирования и туда записываем всю инфу
        for key, value in sd.items():
            f.write(key + ' - ' + ', '.join(value) + '\n')  #записываем в файл
            print(key +'-'+','.join(value))
z1(), z2(), z3()