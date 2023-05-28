def z1():
    class restaurant:   #создаем класс с именем ресторан
        def __init__(self, restaurant_name, cuisine_type): #конструктор, вызывается при создании нового  класса
            self.restaurant_name = restaurant_name    #создаём 1 атрибут - название ресторана
            self.cuisine_type = cuisine_type   #создаём 2 атрибут - тип кухни

        def describe_restaurant(self):
            print(f'{self.restaurant_name} - {self.cuisine_type}')   #название и тип кухни

        def open_restaurant(self):
            print(f'{self.restaurant_name}, Ресторан открыт!')   #название и что ресторан открыт

    newrestaurant = restaurant('Название: Хозяйский', 'Тип кухни: Европейская кухня')
    print(newrestaurant.restaurant_name)  #вывод 1го атрибута - названия
    print(newrestaurant.cuisine_type)  #вывод 2го атрибута - типа кухни
    newrestaurant.describe_restaurant()  #вызов 1го метода - где и название и тип кухни
    newrestaurant.open_restaurant() #вызов 2го метода - где название и что ресторан открыт

def z2():
    class rest:
        def __init__(self, restaurant_name, cuisine_type):    #повторяем что делали в 1 задании
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'{self.restaurant_name} - {self.cuisine_type}')

        def open_restaurant(self):
            print(f'{self.restaurant_name}, Ресторан открыт!')

    restaurant1 = rest('Шаркс', 'Азиатская кухня')   #1 атрибут
    restaurant1.describe_restaurant()                #вывод
    restaurant2 = rest('Абрикос', 'Русская кухня')   #2 атрибут
    restaurant2.describe_restaurant()                #вывод
    restaurant3 = rest('Токио Сити', 'Кавказская кухня') #3 атрибут
    restaurant3.describe_restaurant()                #вывод

def z3():
    class rest:
        def __init__(self, restaurant_name, cuisine_type, rating):  #добавляем к классу ещё и рейтинг
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f'{self.restaurant_name} - {self.cuisine_type}')    #название и тип кухни
            print(f'Рейтинг ресторана: {self.rating}')        #рейтинг

        def open_restaurant(self):
            print(f'{self.restaurant_name}, Ресторан открыт!')  #ресторан открыт

        def rating_set(self, new_rating):
            self.rating = new_rating

        def raiting(self):
            print(f'Новый рейтинг:{self.rating}')   #поле для ввода нового рейтинга

    newrest = rest('Абрикос', 'Русская кухня', 4)  #вывод названия, типа кухни и значение рейтинга
    newrest.describe_restaurant() #вывод названия, типа кухни и значение рейтинга
    newrest.rating_set(input('Введите новый рейтинг:'))   #поле для ввода рейтинга
    newrest.raiting()  #вывод нового рейтинга

z1()
