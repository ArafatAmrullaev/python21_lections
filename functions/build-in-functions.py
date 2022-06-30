"==============Build in functions================"


'lambda' # Анонимная функция
# lambda параметры: что функция возвращает
add = lambda a, b: a + b
print(add(5, 4)) # 9


'map' # Функция, которая принимает первым аргументом функцию, вторым итерируемый объект. map возвращает генератор, в котором все элементы - результат принимаемой функции, в которую мы передали элемент из последовательности

map_gen = map(int, (['1', '2', '3', '4']))
print(map_gen) # <map object at 0x7fc383828dc0>
print(list(map_gen)) # [1, 2, 3, 4]

res = list( map(lambda a: a + 1, [1, 2, 3, 4, 5]) )
print(res) # [2, 3, 4, 5, 6]


"==============map на цикле for================"
func = lambda a: a+1
# def func(a):
#    return a + 1
res = []

for i in [1, 2, 3, 4, 5]:
    res.append(func(i))
print(res) # [2, 3, 4, 5, 6]



'filter' # Функция, которая возвращает генератор, принимает функцию и итерируемый объект. Результатом будет последовательность из элементов итерируемого объекта, которые прошли фильтр(проверку)

vowels = 'ЁУЕЫАОЭЯИЮEYUOAI'
list_ = ['Эртай', 'Оомат', 'Арген', 'Манас', 'Бекзат', 'Даниэль', 'Эркайым']
def startswith_vowels(name):
    vowels = 'ЁУЕЫАОЭЯИЮEYUOAI'
    if name[0].upper() in vowels:
        return True
    return False

res = list(filter(startswith_vowels, list_))
print(res) # ['Эртай', 'Оомат', 'Арген', 'Эркайым']

res = list(filter(lambda name: name.upper().startswith(tuple(vowels)), list_))
print(res) # ['Эртай', 'Оомат', 'Арген', 'Эркайым']


"==============filter на цикле for================"
list_ = ['Эртай', 'Оомат', 'Арген', 'Манас', 'Бекзат', 'Даниэль', 'Эркайым']
def startswith_vowels(name):
    vowels = 'ЁУЕЫАОЭЯИЮEYUOAI'
    if name[0].upper() in vowels:
        return True
    return False
res = []
for name in list_:
    if startswith_vowels(name):
        res.append(name)
print(res) # ['Эртай', 'Оомат', 'Арген', 'Эркайым']


'reduce' # Нужно импортировать из библиотеки functools
# Эта функция принимает функцию и итерируемый объект и возвращает 1 результат

from functools import reduce

list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def mult(a, b):
    return a * b

res = reduce(mult, list_)
print(res) # 362880


"==============reduce на цикле for================"
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def mult(a, b):
    return a * b

res = list_[0]

for b in list_[1:]:
    res = mult(res, b)
print(res) # 362880


'enumerate' # Функция, которая принимает последовательность. Возвращает генератор, в котором каждый элемент - tuple, состоящий из числа и элемента из последовательности
# (enumerate нумерует элементы по дефолту начиная с 0)

list_ = ['a', 'b', 'c', 'd']

for i in enumerate(list_):
    print(i)
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')

for index, elem in enumerate(list_):
    print('Index - ', index, 'Elem - ', elem)
# Index -  0 Elem -  a
# Index -  1 Elem -  b
# Index -  2 Elem -  c
# Index -  3 Elem -  d

for i in enumerate(list_[1:], 10):
    print(i)
# (10, 'b')
# (11, 'c')
# (12, 'd')


'zip' # соединяет последовательности 
list1 = [1, 2, 3, 4, 5, 6]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
print(list(zip(list1, list2))) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f')]
print(dict(zip(list1, list2))) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}
print(zip(list1, list2)) # <zip object at 0x7f8a5377cf00>

list1 = [1, 2, 3, 4, 5, 6]
list2 = ['a', 'b', 'c']
print(list(zip(list1, list2))) # (1, 'a'), (2, 'b'), (3, 'c')]

list1 = [1, 2, 3, 4, 5, 6]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
list3 = [1.9, 2.7, 3.0, 4.5]
print(list(zip(list1, list2, list3))) # [(1, 'a', 1.9), (2, 'b', 2.7), (3, 'c', 3.0), (4, 'd', 4.5)]