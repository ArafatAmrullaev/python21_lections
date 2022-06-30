from decimal import Decimal
k = 'o'
while k == 'o':
    a = Decimal(input('Введите первое число:'))
    c = input('Выберите операцию из следующих +, -, *, /, %, **, // :')
    b = Decimal(input('Введите второе число:'))
    if c == '+':
        print('Ответ:',a + b)
    elif c == '-':
        print('Ответ:',a - b)
    elif c == '*':
        print('Ответ:',a * b)
    elif c == '/':
        print('Ответ:',a / b)
    elif c == '**':
        print('Ответ:',a ** b)
    elif c =='//':
        print('Ответ:',a // b)
    elif c == '%':
        print('Ответ:',a % b)
    else:
        print('Данной операции нет в системе')
    k = input('Введите "o", чтобы продолжить')