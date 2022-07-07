continue_play = True
answers = [ '1799',    '1821',     '1809',   '1982',     '1870']
writers = ['Пушкин','Достоевский','Гоголь','Ломоносов','Куприн']
max_prise = 5
while continue_play == True:
    prise = 0
    for i in range(len(writers)):
        your_answer = input(f'В каком году родился {writers[i]}?')
        if your_answer == answers[i]:
            prise += 1
    print(f'Правильных ответов: {prise}')
    print(f'Ошибок: {max_prise-prise}')
    print(f'Процент верных ответов: {(prise/max_prise)*100}%')
    print(f'Процент неверных ответов: {(max_prise-prise)*100/max_prise}%')
    if input('Хотите сыграть ещё раз? ( Y/N )') == 'N':
        continue_play = False
