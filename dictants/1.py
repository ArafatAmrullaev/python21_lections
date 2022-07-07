""" 
Создать список из чисел в диапазоне от 1 до 10
"""
# 1 
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1.2
list1 = list(range(1, 11))

# 1.3
list1 = [*range(1, 11)]

# 1.4
list1 = [i for i in range(1, 11)]

# 1.5
list1 = []
for i in range(1, 11):
    list1.append(i)

# 1.6
string1 = '1 2 3 4 5 6 7 8 9 10'
list1 = list( map(int, string1.split()) )


"""
Найти сумму всех чисел в списке
"""
# 2
list_sum = sum(list1)

# 2.2
from functools import reduce
from math import remainder
list_sum = reduce( lambda x, y: x+y, list1 )

# 2.3
list_sum = 0
for i in list1:
    list_sum += i


"""
Запросите число у пользователя
"""
num = int(input('Введите число: '))


"""
Найти остаток от деления суммы на число
"""
# 3
remainder = list_sum%num

# 3.2
div, remainder = divmod(list_sum, num)


"""
В список добавить по индексу 2 число 11
"""

# 4
list1.insert(2, 11)

# 4.2
list1 = list1[:2] + [11] + list1[2:]

# 4.3
new_list = []
index = 0
for i in list1:
    if index == 2:
        new_list.append(11)
    new_list.append(i)
    index += 1


"""
Заменить значение в списке под индексом 5 на строку 'hello'
"""

# 5
list1[5] = 'hello'

# 5.2
list1.pop(5)
list1.insert(5, 'hello')

# 5.3
list1 = list1[:5] + ['hello'] + list1[6:]

# 5.4
class My_list(list):
    def replace(self, index, value):
        self[index] = value

list1 = My_list(list1)
list1.replace(5, 'hello')
print(list1)


"""
Поднять в верхний регистр строку в списке
"""
# 6
upp = list1[5].upper()

# 6.2
upp = ''
for i in list1:
    if type(i) == str:
        upp = i.upper
        

# 6.3
class Mylist(list):
    def get(self, index, default=None):
        try:
            return self[index]
        except:
            return default

list1 = Mylist(list1)
upp = list1.get(5, '').upper()


# 6.4
strings = list(filter(lambda x: type(x) == str, list1))
upp = [s.upper() for s in strings]


"""
Создайте список с числами от 1 до 10 в виде строк
"""
# 7
list2 = ['1', '2', '3', '4', '5']

# 7.2
list2 = '1 2 3 4 5'.split()

# 7.3
list2 = list('12345')

# 7.4
list2 = list( map(str, range(1,6)) )

# 7.5
list2 = list( map(lambda x: str(x), range(1,6)) )

# 7.6 
list2 = [str(i) for i in range(1, 6)]

# 7.7
list2 = []
for i in range(1, 6):
    list2.append(str(i))


"""
Переведите каждый элемент в списке в число
"""
# 8
list3 = [1, 2, 3, 4, 5]

# 8.2
list3 = [int(i) for i in list2]

# 8.3
list3 = list(map(int, list2))

# 8.4
list3 = []
for i in list2:
    list3.append(int(i))


"""
Создайте класс Person с атрибутами класса arms = 2, legs = 2 и атрибутом объекта name
"""
# 9
class Person:
    arms = 2
    legs = 2
    def __init__(self, name):
        self.name = name

# 9.2
class Person:
    arms = 2
    legs = 2
    name = None

obj = Person()
obj.name = 'Arafat'


"""
Создайте объект от класса со своим именем
"""
arafat = Person('Arafat')
