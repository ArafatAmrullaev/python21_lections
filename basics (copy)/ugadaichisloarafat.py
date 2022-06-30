import random
a = input('Введите ваше имя: ')
b = input(f'{a}, хотите ли вы играть?(Введите Да или Нет):  ')
r = random.randint(1, 10)
while b == 'Да':
    for i in range(1, 6):
        g = 6 - i
        print(f'{a}, у вас осталось попыток: {g} ')
        c = int(input(f'{a}, угадайте число от 1 до 10:  '))
        if r == c:
            print(f'{a}, вы победили! Число угадано. Вам потребовалось попыток: {i}')
            r = random.randint(1, 10)
            break
        else:
            print(f'{a}, вы проиграли!')
            continue
    b = input(f'{a}, хотите поиграть еще раз?(Введите Да или Нет):  ')
print(f'До свидания, {a}!')