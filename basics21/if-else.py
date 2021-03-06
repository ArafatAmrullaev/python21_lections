"===================Логические операторы==================="
# Логические операторы - выражения, которые возвращают True, если правда, False - если ложь
 
5 == 5 # True
4 == 5 # False

5!=5 # False
5!=2 # True

5 > 10 # False
10 > 5 # True
5 > 5 # False

5 < 10 # True
10 < 5 # False
5 < 5 # False
  
5 <= 10 # True
10 <= 5 # False
5 <= 5 # True

5 >= 10 # False
10 >= 5 # True
5 >= 5 # True

'5' == 5 # False


"===================Boolean Type==================="
# Булевый тип данных имеет всего 2 значения: True и False
bool(1) # True
bool(0) # False
bool(-277) # True

bool('hello') # True
bool('') # False
bool(' ') # True

bool(True) # True
bool(False) # False


"===================None Type==================="
# None - тип данных с одним значением None, который используется для обозначения пустых значений или отсутствия значений
bool(None) # False
bool('None') # True

a = None
print(bool(a)) # False
print(a is None) # True
# is - проверка на полное соответствие


"===================Условные операторы==================="
# Условные операторы нужны для того, чтобы при разных входных данных код работал по разному
if условие1:
    тело1
    # Будет работать, если условие 1 верно

if условие1:
    тело1
else:
    тело2
    # Будет работать, если условие 1 неверно

if условие1:
    тело1
elif условие2:
    тело2
    # Будет работать, если условие 1 неверно и условие 2 верно


if условие1:
    тело1
elif условие2:
    тело2
else:
    тело3
    # Будет работать, если условие 1 и условие 2 неверно

# В одной конструкции мы можем использовать неограниченное количество elif или можно не указывать
# В одной конструкции мы можем использовать только один if
# else  также используется только один раз или можно не указывать

a = int(input('Введите число: '))

if a>0:
    print(f'Число {a} - положительное')
elif a<0:
    print(f'Число {a} - отрицательное')
else:
    print(f'Число {a} - 0')


"===================FizzBuzz==================="
# Выведите числа от 1 до 100
# Если число кратно 3 - вывести Fizz
# Если число кратно 5 - вывести Buzz
# Если число кратно 3 и 5 - вывести FizzBuzz
# Если число не кратно ни 3, ни 5 - вывести число

# for i in range(1, 101):
#     if (i)%3 == 0 and (i)%5 != 0:
#         print('Fizz')
#     elif (i)%5 == 0 and (i)%3 != 0:
#         print('Buzz')
#     elif (i)%5 == 0 and (i)%3 == 0:
#         print('FizzBuzz')
#     else:
#         print(i)

for i in range(1, 101):
    if (i)%5 == 0 and (i)%3 == 0:
        print('FizzBuzz')
    elif (i)%5 == 0:
        print('Buzz')
    elif (i)%3 == 0:
        print('Fizz')
    else:
        print(i)

"=============And or not================="
# and - и
# or - или
a = 5
b = 6

a == 5 and b == 6 # True (правая сторона True, левая тоже True)
a == 5 and b == 5 # False (правая сторона True, но левая False)
a == 4 and b == 5 # False (обе стороны False)

a == 5 or b == 6 # True (правая сторона True, левая тоже True)
a == 5 or b == 5 # True (правая сторона True, но левая False)
a == 4 or b == 5 # False (обе стороны False)

# если обе части выдают True - будет True
# если обе части выдают False - будет False
# если одна часть True, вторая False:
# 1. если стоит and - выйдет False
# 2. если стоит or - выйдет True

not True # False
not False # True
not a == 5 # False (потому что a == 5)
not a == 4 # True (потому что a == 5)


2 in [1, 2, 3, 4, 5] # True
'a' in {'b':3, 'c':'a'} # False: 'a' нет среди ключей



"====================Тернарные операторы==================="
# Условия в одну строку
тело1 if условие else тело2

res = 'Hello' if a == 5 else 'Bye'
print(res)
# Hello если а == 5
# Bye если а != 5
