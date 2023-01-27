

##level_1, level_2, level_3, level_4 = 1, 2, 3, 4 # Уровни персонажа
##
##score = int(input('Введите количество опыта: '))
##
##if score < 1000:
##  print('Ваш уровень:', level_1)
##elif score >= 1000 and score < 2500:
##  print('Ваш уровень:', level_2)
##elif score >= 2500 and score < 5000:
##  print('Ваш уровень:', level_3)
##else:
##  print('Ваш уровень:', level_4)

##x = int(input('Введите икс: ')) # вводим значение икс для расчёта функции y= {x −12, x>0, 5,  x=0 x2,  x<0 
##
##if x == 0:
##  print('Игрек равен', 5)
##elif x < 0:
##  print('Игрек равен', x ** 2)
##else:
##  print('Игрек равен', x - 12)


##place = int(input('Введите место в списке поступающих: '))
##score = int(input('Введите количество баллов за экзамены: '))

##if place <= 10:
##  print('Поздравляем, Вы поступили!')
##  if score >= 290:
##    print('Бонусом Вам будет начисляться стипендия')
##  else:
##    print('Но Вам не хватило баллов для стипендии')
##else:
##  print('К сожалению, вы не поступили.')


##
##rating = int(input('Что получил по математике? '))
##if rating == 2 or rating == 3:
##    print('Плохо. Марш учиться!')
##elif rating == 4 or raiting == 5:
##    print('Молодец! Можешь отдохнуть.')
##
##number_1 = int(input('Введите первое число: '))
##number_2 = int(input('Введите второе число: '))
##number_3 = int(input('Введите третье число: '))
##
##if number_1 == number_2 and number_1 == number_3:
##  print('3')
##elif (number_1 == number_2) or (number_1 == number_3) or (number_2 == number_3):
##  print('2')
##else:
##  print('0')

##
##square = int(input('Введите площадь квартиры в кв.м: '))
##price = int(input('Укажите стоимость квартиры в рублях: '))
##
##if square >= 100 and price <= 10000000:
##  print('Подходящий вариант квартиры побольше.')
##elif square >= 80 and price <= 7000000:
##  print('Подходящий вариант квартиры поменьше.')
##else:
##  print('Вариант не подходит.')

time = int(input('Укажите время для получения посылки: '))

if (time >= 8) and (time < 10) or (time >= 12) and (time < 14) or (time >= 15) and (time < 18) or (time >= 20) and (time < 22):
 print('Можно получить посылку')
else:
 print('Посылку получить нельзя.')

# time = int(input('Укажите время для получения посылки: '))

# if (time > 21) or (time < 8) or (time >= 10) and (time < 12) or (time > 13) and (time < 15) or (time > 17) and (time < 20):
#   print('Посылку получить нельзя.')
# else:
#   print('Можно получить посылку')














