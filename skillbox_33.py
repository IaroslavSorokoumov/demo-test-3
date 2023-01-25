##
##def greeting():
##
##    print('Привет!')
##
##    print('Добро пожаловать!')
##
##
##while True:
##
##    a = input('Зайдёте? Да/Нет: ')
##
##    if a == 'Да':
##
##        greeting()
##
##    print('Следующий.\n')

##def supply():
##    a = int(input())
##
##    b = int(input())
##
##    print("Всего", a+b, "шт.\n")
##    
##
##print("Сколько мешков рыбы и мяса?")
##supply()
##
##print("Сколько буханок белого и чёрного хлеба?")
##supply()
##
##print("Сколько вёдер воды и молока?")
##supply()

##def name_addr(surname, name, street, house):
##    print(f"\nФамилия: {surname}\n"
##          f"Имя: {name}\n"
##          f"Улица: {street}\n"
##          f"Дом: {house}")
##
##surname = input('Укажите фамилию: ')
##name = input('Укажите имя: ')
##street = input('Улица: ')
##house = input('Дом: ')
##
##for _ in range(3):
##    name_addr(surname, name, street, house)
##


##def aboutWater(price):
##    print(f"\nНазвание: КлирВотер\n"
##          f"Производитель: ВодЗавод\n"
##          f"Цена: {price}\n")
##
##for _ in range(3):
##    price = input('Какая цена: ')
##    aboutWater(price)

##from math import pi as pi
##
##def sphereArea(radius):
##    s = 4 * pi * radius ** 2
##    print('\nПлощадь поверхности сферы =', s, 'кв.км')
##
##def sphereVolume(radius):
##    v = (4 / 3) * pi * radius ** 3
##    print('Объём сферы =', v, 'куб.км')
##
##radius = float(input('Укажите радиус планеты: '))
##sphereArea(radius)
##sphereVolume(radius)

from math import sqrt as sqrt

def isPrime(number):
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

numbers = int(input('Укажите кол-во чисел: '))
counter = 0
for _ in range(numbers):
    number = int(input('Введите число для проверки: '))
    if isPrime(number):
        counter += 1

print('Кол-во простых чисел:', counter)

        
        
























