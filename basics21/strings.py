"===================Строки==================="
# Строки - неизменяемый тип данных, который предназначен для хранения текста (последовательности символов), заключенного в одинарные или двойные кавычки
# Синтаксис:
string = 'Пример'
string2 = "Пример2"
# error = 'Неправильная строка"
string3 = "Don't" # Внутри двойных кавычек все одинарные просто символы
string4 = '"Makers"' # Внутри одинарных все двойные - символы
string5 = '''
Многострочный текст
в одинарных кавычках
Тут можно ставить "любые" 'кавычки'
''
""""
'''
string6 = """
Многострочный текст
в одинарных кавычках
Тут можно ставить "любые" 'кавычки'
'''
""
"""

string7 = 'hello' + ' ' + 'world' # 'hello world'
string6 = 'A' + 5 # 'AAAAA'


"===================Экранизация строк==================="
# Экранизация спецсимволов
'\n' # Перенос на новую строку
'\t' # Табуляция(4 пробела)
'\\' # Отображение \ (потому что является инструкцией для python, которая влияет на наш код)
'\'' # Отображение '
"\"" # Отображение "
'\r' # Возвращение каретки в начало строки
'\v' #  Перенос на новую строку со смещением вправо на длину первого слова

'Hello\nworld'
#Hello
#world

'Hello\tworld'
#Hello  world

'Чтобы экранизировать нужен символ \\'
#Чтобы экранизировать нужен символ \

'My website is Latracal \rSolution'
#Solutionte is Latracal

'Hello\vworld'
#Hello
#     world


"===================Форматирование строк==================="
title = 'Плов'
price = 1500
f'Название: {title}, Цена: {price}'
# Название: Плов, Ценв: 1500

format1 = f'Название: {title}, Цена: {price}'
format2 = 'Название: %s, Цена: %s'
print(format2 % ('Гуляш', "250"))
print(format2 % ('Самсы', "70"))
# Название: Гуляш, Цена: 250
# Название: Самсы, Цена: 70

format3 = 'Название: {}, Цена: {}'
print(format3.format('Шакарап', '35'))
# Название: Шакарап, Цена: 35


"===================Методы строк==================="
# Методы типов данных - функции, к которым мы обращаемся через точку
dir(str) # Позволяет посмотреть все методы класса

'HELLO'.lower() # 'hello'
'hello'.upper() # 'HELLO'
'Hello'.swapcase() # 'hELLO'
'heLLo'.title() # 'Hello'
'heLLo wOrlD'.title() # 'Hello World'
'hello world'.capitalize() # 'Hello world'

'hello'.center(11) # '   hello   '
'hello'.center(11,'-') # '---hello---'

'hello'.count('l') # 2
'hello'.count('ll') # 1
'hello hello'.count('hello') # 2

'hello world'.startswith('hell') # True
'hello world'. endswith('ld') # True

'hello world'.find(' ') # 5
'hello world'.find('o') # 4
'hello world'.find('wo') # 6
'hello world'.find('hello world') # 0

'hello world'.split() # ['hello', 'world']
'hello world'.split('o') # ['hell', ' w', 'rld']

'$'.join(['hello', 'world']) # 'hello$world'
' '.join(['hello', 'world']) # 'hello world'
''.join(['hello', 'world']) # 'helloworld'

# Конкатенация - склеивание строк
'hello' + 'world' # helloworld
'hello' + ' ' + 'world' # hello world


"===================Индексы==================="
# Индекс - порядковый номер символва в строке
'h e l l o   w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
string = 'hello world'
string[0] # h
string[10] # d
string[5] # ' '

# срез - подстрока строки
string[0:5] # 'hello'
string[0:6] # 'hello '
string[2:4] # 'll'string[0:5] # 'hello'
string[0:5][2:4] # 'll'
string[:5] # 'hello'
string[6:] # 'world'
string[:] # 'hello world'
string[0:11:2] # 'hlowrd'
string[::3] # 'hlwl'
string[::-1] # 'dlrow olleh'
string[::-2] # 'drwolh'





"===================Доп инфа==================="
a = 5
b = 5
print(id(a))
print(id(b))
print(hash(a))
print(hash(b))
id(a) == id(b)
hash(a) == hash(b)