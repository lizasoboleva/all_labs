def z1():
    class Restaurant:  #создаем класс ресторан как в прошлом задании
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')
    class IceCreamStand(Restaurant):  #создаем класс кафе - мороженное
        def __init__(self, restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors
        def ice_flavors(self):  #добавляем атрибут для хранения списка сортов мороженого
            print('Вкусы мороженого:')
            print(*self.flavors, sep='\n')  #вывод сортов мороженного
    a = IceCreamStand('Мороженое', 'Кафе', ['Ванильное', 'Шоколадное', 'Фисташковое', 'Клубничное'])
    a.ice_flavors()

def z2():
    class Restaurant:  #снова создаем класс ресторан
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')

    class IceCreamStand(Restaurant):  #создаем класс мороженное
        def __init__(self, restaurant_name, cuisine_type, flavors, loc, time):  #но добавляем ещё место и время работы
            super().__init__(restaurant_name, cuisine_type)  #возвращает объект объект-посредник, который делегирует вызовы метода родительскому или родственному классу, указанного типа
            self.flavors = flavors  #сорта мороженного
            self.place = loc   #место
            self.time = time   #часы работы

        def ice_flavors(self):
            print('Виды мороженного: ')
            print(*self.flavors, sep='\n')

        def newflavor(self):  #добавляем метод для ввода нового сорта из списка flavors
            self.flavors.append(input('Введите новый сорт мороженного:'))

        def delflavor(self):   #добавляем метод для удаления сорта из списка flavors
            self.flavors.remove(input('Введите сорт, который хотите удалить:'))

        def poisk(self):  #добавляем метод для проверки наличия сорта мороженного
            if input('Введите какой вкус хотите найти:') in self.flavors:
                print('В наличии')
            else:
                print('Нет в наличии')

    class napalochke(IceCreamStand):  #создаем класс для мороженного на палочке
        def __init__(self, restaurant_name, cuisine_type, flavors, loc, time, material):
            super().__init__(restaurant_name, cuisine_type, flavors, loc, time)
            self.material = material   #добавляем материал палочки

        def palka(self):
            print('Материал палочки:', self.material)

    a = IceCreamStand('Мороженное', 'Кафе', ['Ванильное', 'Шоколадное', 'Фисташковое', 'Клубничное'], 'пр. Невский', '9:00-21:00')
    a.describe_restaurant()
    a.newflavor()
    a.ice_flavors()
    a.delflavor()
    a.ice_flavors()
    a.poisk()

    b = napalochke('Мороженное', 'Кафе', ['Ванильное', 'Шоколадное', 'Фисташковое', 'Клубничное'], 'пр. Невский', '9:00-21:00', 'Дерево')
    b.palka()

import tkinter as tk  #используем библиотеку tkinter
def z3():
    class IceCreamStand:
        def __init__(self):
            self.names = ['Нева', 'Свитлогорье', 'Бонпари', 'Коровка из Кореновки', 'Чистая линия', 'Баскин Робинс']
            self.types = ['Ванильное', 'Шоколадное', 'Фруктовый лёд', 'Клубничное', 'Мятное', 'Карамельное']

        def get_names(self):  #марки мороженного
            return self.names

        def get_types(self):   #сорта мороженного
            return self.types

    class IceCreamStandGUI:
        def __init__(self, master):
            self.master = master
            master.title('IceCream')  #заголовок

            self.ice_cream_stand = IceCreamStand()
            self.names_label = tk.Label(master, text='Название', font='Calibri 12 bold')  #в окне задаем название и шрифт
            self.names_listbox = tk.Listbox(master, font='Calibri 12', height=len(self.ice_cream_stand.get_names()))

            for name in self.ice_cream_stand.get_names():
                self.names_listbox.insert(tk.END, name)

            self.types_label = tk.Label(master, text='Вид', font='Calibri 12 bold')
            self.types_listbox = tk.Listbox(master, font='Calibri 12', height=len(self.ice_cream_stand.get_types()))

            for type in self.ice_cream_stand.get_types():
                self.types_listbox.insert(tk.END, type)

            self.names_label.grid(row=0, column=0)   #заполняем таблицу
            self.names_listbox.grid(row=1, column=0)
            self.types_label.grid(row=0, column=1)
            self.types_listbox.grid(row=1, column=1)

    root = tk.Tk()
    a = IceCreamStandGUI(root)
    root.mainloop()

z2()
