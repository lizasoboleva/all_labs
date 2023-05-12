from PIL import Image, ImageFilter
def n1():
    image = Image.open('babochka.jpg')
    image.show()                 #открываем картинку
    width,height = image.size    #размеры картинки
    forma = image.format         #формат
    mode = image.mode            #цветовая модель

    print('ширина', width)       #выводим параметры картинки
    print('высота', height)
    print('формат', forma)
    print('цветовая модель', mode)

def n2():
    image = Image.open('babochka.jpg')                            #открываем картинку
    image.show()
    new = image.resize((image.width // 3, image.height // 3))     #меняем ширину и высоту картинки
    new.save('new.png')                                           #сохраняем в новый файл новые размеры
    con = image.rotate(180)                                       #поворачиваем картинку на 180
    con.save('newflip.jpg')                                       #сохраняем в новый файл с поворотом
    con = image.transpose(Image.FLIP_LEFT_RIGHT)                  #зеркалим
    con.save("newflip1.jpg")                                      #сохраняем в новый файл

def n3():
    names = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]  #записываем исходные файлы в переменную
    for file in names:
        with Image.open(file) as img:
            img.load()                                      #загружаем картинки и применяем к ним фильтр контура
            new1 = img.filter(ImageFilter.CONTOUR)
            new1.show()
            new1.save('new' + file)                         #сохраняем под новым названием отформатированные картинки

def n4():
    image1 = Image.open('water.png')                                #открываем сам водяной знак
    new1 = image1.resize((image1.width // 4, image1.height // 4))   #изменяем размеры
    img = Image.open("1.jpg")                                       #открываем любую картинку, чтобы вставить водяной знак
    img.paste(new1)
    img.save("waterbabochka.jpg")                                   #сохраняем новый файл с водяным знаком
    img.show()
n1(),n2(),n3(),n4()