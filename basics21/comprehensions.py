"==============Comprehensions================"
# comprehensions - генерация последовательностей в одну строку используя цикл

# 1. результат for элемент in итерируемый объект
# 2. результат for элемент in итерируемый объект if фильтр


"==============List comprehensions================"

# Создать список, состоящий из чисел от 1 до 10
from operator import index


list_ = []
for i in range(1, 11):
    list_.append(i)
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_ = list( (i for i in range(1, 11)) )
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_ = [ (i for i in range(1, 11)) ]
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Создать список, состоящий из четных чисел от 1 до 10
list_ = []
for i in range(1, 11):
    # if not 0 (четное)
    if not i % 2:
        list_.append(i)
# list_ = [2, 4, 6, 8, 10]

list_ = [ i for i in range(1, 11) if not i%2]
# list_ = [2, 4, 6, 8, 10]

list_ = [i for i in range(2, 11, 2)]
# list_ = [2, 4, 6, 8, 10]

list_ = [print(i) for i in range(10)]
# 0 1 2 3 4 5 6 7 8 9
print(list_)
# [None, None, None, None, None, None, None, None, None, None]

list_ = ['hello' for i in range(10)]
# [hello, hello, hello, hello, hello, hello, hello, hello, hello, hello]

print([input() for i in range(10)])
# На каждой итерации запрашивает инпут


# Создать список, состоящий из чисел от 1 до 10, но вместо чисел написать 'четное' или 'нечетное'
list_ = ['нечетное' if i % 2 else 'четное' for i in range(1, 11)]
print(list_)
# ['нечетное', 'четное', 'нечетное', 'четное', 'нечетное', 'четное', 'нечетное', 'четное', 'нечетное', 'четное']

# Создать список из чисел, находящихся в list1, заменив их на 'четное' или 'нечетное'
list1 = [1, 'hello', 3, 'a', 4.0, 6, 8, 'hw']
list_ = ['нечетное' if i % 2 else 'четное' for i in list1 if type(i) == int or type(i) == float]
print(list_)
# ['нечетное', 'нечетное', 'четное', 'четное', 'четное']


"==============Dict comprehensions================"
# Создать словарь, где ключи - числа от 1 до 10, а значения это числа в виде строки
dict_ = dict((i, str(i)) for i in range (1, 11))
print(dict(dict_))
# {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10'}

# Даны 2 списка. Создайте словарь, где ключи - элементы первого списка, а значения - второго
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

dict_ = dict( (list1[index], list2[index]) for index in range(len(list1)))
print(dict_)
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

dict_ = { list1[index]: list2[index] for index in range(len(list1))}
print(dict_)
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

# Создайте копию слова
dict1 = {'a':1, 'b': 2, 4:'c'}
dict2 = { key: value for key, value in dict1.items()}
print(dict2)
# {'a': 1, 'b': 2, 4: 'c'}

# Поменяйте ключ и значение местами
dict2 = { value: key for key, value in dict1.items()}
print(dict2)
# {1: 'a', 2: 'b', 'c': 4}

# Дан словрь, где значения - список с числами. Создайте новый словарь, где значения - сумма тех чисел
dict1 = {
    'a':[1, 2, 3, 4, 5], 
    'b':[21, 20, 40], 
    'c':[22, 76, 45], 
    'd':[3, 45, 5]
    }
dict2 = { key: sum(value) for key, value in dict1.items()}
print(dict2)
# {'a': 15, 'b': 81, 'c': 143, 'd': 53}


"==============Вложенные comprehensions================"
# Создайте словарь, где ключами будут числа от 1 до 10, а значениями списки от 1 до числа {который ключ}

dict_ = {   i: list(range (1, i + 1)) for i in range(1, 6) }
print(dict_)
# {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}

dict_ = {   i: [j for j in range(1, i+1)] for i in range(1, 6) }
print(dict_)
# {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}

# Создайте список, состоящий из 10 списков, в которых строка 'hello world' повторяется 5 раз

list_ = [
    ['hello world' for i in range(5)]
    for i in range(10)if a.get(key) == 3 

]
print(list_)
# [['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world'], ['hello world', 'hello world', 'hello world', 'hello world', 'hello world']]


list_ = [
    [i for i in range(5)]
    for i in range(10)

]
print(list_)
# [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]