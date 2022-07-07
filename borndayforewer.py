while True:
    dr_year_writer = input('Когда родился А.С.Пушкин?')
    if dr_year_writer == '1799':
        print('Верно!')
        while True:
            dr_day_writer = input('Введите день рождения А.С.Пушкина:')
            if dr_day_writer == '6 июня':
                print('Верно!')
                break
            else:
                print('Не верный день рождения')
        break
    else:
        print('Не верный год')