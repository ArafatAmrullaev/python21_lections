import random
words = ['стекло', 'солнце', 'яблоко', 'дерево', 'динозавр', 'песочница', 'кабина', 'дебют', 'винил', 'треугольник', 'приложение', 'кондиционер']
word = random.choice(words)
hangman = [
""" 
-------
|    |
|
|
|
|
|
|
---------
""",
""" 
-------
|    |
|    O
|    |
|
|
|
|
---------
""",
""" 
-------
|    |
|    O
|    |
|   /
|
|
|
---------
""",
""" 
-------
|    |
|    O
|    |
|   / /
|
|
|
---------
""",
""" 
-------
|    |
|    O
|    |
|   /|/
|    | 
|   / 
|
---------
""",
""" 
-------
|    |
|    O
|    |
|   /|/
|    | 
|   / /
|
---------
""",
]
attempts = 5
b = 0
hhh = len(word) * '*'

print('Добро пожаловать в виселицу!')
des = input('Хотите поиграть? Введите Да или Нет: ').capitalize()
if des == 'Да':
    print('Вы должны угадать слово.')
while des == 'Да':
    print(hhh)
    let = input('Введите букву: ')
    if let in word.lower():
        if let == '':
            print('Введите букву! ')
        else:
            print('Данная буква есть в слове!')
        hh = ''
        for i in range(len(word)):
            if let == word[i]:
                hh = hh + let
            else:
                hh = hh + hhh[i]
        hhh = hh
        if hhh == word:
            print(hhh)
            print(f'Поздравляю! Вы угадали слово "{word}"!')
            des = input('Хотите снова поиграть? Введите Да или Нет: ').capitalize()
            attempts = 5
            b = 0
            let1 = ''
            word = random.choice(words)
            hhh = len(word) * '*'
    else:
        attempts = attempts - 1
        b = b + 1
        hangg = hangman[b]
        print(f'Данной буквы нет в слове. У вас осталось попыток: {attempts}')
        print(hangg)
    if attempts == 0:
        print('Вы проиграли!')
        print(f'Загаданным словом было {word}')
        des = input('Хотите снова поиграть? Введите Да или Нет: ').capitalize()
        attempts = 5
        b = 0
        let1 = ''
        word = random.choice(words)
        hhh = len(word) * '*'
print('До свидания! Хорошего дня!')