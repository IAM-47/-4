import datetime

date_pr = input('Введите дату прибытия поезда: ')
date_ot = input('Введите дату отбытия поезда: ')

try:
    res = datetime.datetime.strptime(date_pr, '%Y-%m-%d--%H:%M')
    res2 = datetime.datetime.strptime(date_ot, '%Y-%m-%d--%H:%M')
    resres = res2 - res
except ValueError:
    print('Формат введенной даты не соответствует положенному!')
else:


    print(resres)
