dr_year_writer = input('Когда родился А.С.Пушкин?')
if dr_year_writer == '1799':
    print('Верно!')
    dr_day_writer = input('Введите день рождения А.С.Пушкина:')
    if dr_day_writer == '6 июня':
        print('Верно!')
    else:
        print('Не верный день рождения')
else:
    print('Не верный год')