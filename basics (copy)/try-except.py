"================Исключения=================="
# Исключения (ошибки) - объекты, которые прерывают работу кода, если были вызваны


SyntaxError # исключение, которое выходит, когда в коде допущена синтаксическая ошибка

# (  - SyntaxError: unexpected EOF while parsing
# (когда мы не закрыли скобочку или кавычку)
# a =    - SyntaxError: invalid syntax
# (когда мы что-то сделали не по синтаксису питона)

NameError # исключение, которое выходит, когда мы обращаемся по несуществуещему индексу

list_ = [1, 2, 3, 4]
# list_[1000]    - IndexError: lost index out of range
# list_.pop(1000) - IndexError: pop index out of range

dict_ = {'a':1}
# dict_['b']  -  KeyError: 'b'
# dict_.pop('b')  - KeyError: 'b'

print(dict_.get('b')) # не ошибка, выйдет None, если ключа нет

ValueError # выходит, когда мы пытаемся распаковать какую-то последовательность, где количество переменных и элементов в последовательности не совпадают или когда мы в функцию передаем некорректный для нее тип данных

# a, b, c = 'ab'   - ValueError: not enough values to unpack (expected 3, got 2)
a, b = 'ab' # 2 символа могут распаковаться на две переменные 
# int('hello')   - ValueError: invalid literal for int() with base 10: 'hello'

TypeError # выходит, когда мы пытаемся использовать методы не свойственные какому-то типу данных
# или когда мы пытаемся передать в функцию больше или меньше аргументов, чем принимает функция 

# for i in 12345678:   - TypeError: 'int' object is not iterable

# 5 + '5'   - TypeError: unsupported operand type(s) for +: 'int' and 'str'

# '5' + 5   - TypeError: can only concatenate str (not "int") to str

# hash([1, 2])   - TypeError: unhashable type: 'list'

# input('hello', 1)   - TypeError: input expected at most 1 argument, got 2

# [].append()   - TypeError: append() takes exactly one argument (0 given)

# [].append(1, 2)   - TypeError: append() takes exactly one argument (2 given)

IndentationError # когда мы неправильнр используем отступы

#         a = 4   - IndentationError: unexpected indent

# for i in range(1):
# print(i)   - IndentationError: expected an indented block

ZeroDivisionError # выходит при делении на 0

# 45 / 0  ZeroDivisionError
# 3 // 0  ZeroDivisionError
# 100 % 0  ZeroDivisionError

AttributeError # выходит, когда мы обращаемся к несуществующему атрибуту или методу объекта

# [].replace('a', ' ')   - AttributeError: 'list' object has no attribute 'replace'


"================Обработка исключений=================="
# чтобы код не прекращал свою работу при некорректных данных

# try:
#     код, который может вызвать ошибку

# except Ошибка, которая может возникнуть:
#     код, который сработает, если в try ошибка вышла

# else:
#     код, который сработает, если в try ошибка не вышла

# finally:
#     код, который сработает в любом случае


try:
    num = int(input())
except ValueError:
    print('Введите число!')
else:
    print('Введнное число', num)
# если в input придет число - выйдет то, что мы написали в else
# если в input придет не число - выйдет то, что мы написали в except

# raise  - вызвать ошибке

try:
    raise KeyError
except ValueError:
    print('ValueError')
except TypeError:
    print('TypeError')
except KeyError:
    print('KeyError')

print('after try-except')


try:
    raise ValueError
except (ValueError, TypeError, KeyError): # Отлавливает только те ошибки, которые мы указали
    print('Была обработана одна ошибка из ValueError, TypeError, KeyError')


try:
    raise SyntaxError
except: # Отлавливает все ошибки
    print('Была обработана ошибка') 


try:
    print('hello')
except:
    print('except')
else:
    print('else')   # hello  else


try:
    print('hello')
    raise TypeError
except:
    print('except')  # hello  except
else:
    print('else')   


# try:
#     5 + '5'
# except ValueError:
#     print('ValueError')
# else:
#     print('Все ок')
# finally:
#     print('finally')
# print('finally')
# finally
# Traceback (most recent call last):
#   File "/home/arafat/Desktop/python21-lections/basics/try-except.py", line 132, in <module>
#     5 + '5'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

try:
    5 + '5'
except Exception as error: # отловятся все ошибки + мы их записываем в переменную
    print(error.__class__)  # <class 'TypeError'>
else:
    print('Все ок')
finally:
    print('finally')