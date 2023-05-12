from PIL import Image, ImageDraw, ImageFont

def n1():
    pic = Image.open('открытка.jpg')
    pic2 = pic.crop((20,20,440,440))
    pic2.show()
    pic2.save('открытка2.jpg')

def n2():
    otkr = {
        '8 марта' : '8 марта.jpg',
        '23 февраля': '23 февраля.jpg',
        'Новый Год': 'новый год.jpg',
        '14 февраля': '14 февраля.jpg',
        'День Рождения': 'день рождения.jpg',
    }
    o = []
    prazd = input('Введите название праздника: ')
    if prazd in otkr:
        card = Image.open(otkr[prazd])
        card.show()
    else:
        print('Открытки к данному празднику нет!')

def n3():
    name = input('Как зовут того, кого вы хотите поздравить? ') + ' , поздравляю!'
    pic = Image.open('открытка.jpg')
    pic2 = pic.crop((20,20,440,440))
    draw = ImageDraw.Draw(pic2)
    font = ImageFont.truetype('arial.ttf',36)
    draw.text((50,50), name, font=font, fill=(255,255,255))
    pic2.save('pic2.png')
    pic2.show()

n1(), n2(), n3()