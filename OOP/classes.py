"===================OOP==================="
# OOP - Object-Oriented Programming
# ООП - объектно-ориентированное программирование (парадигма)

class Person:
    name = 'Арафат'
    age = 18
    arms = 2
    legs = 2

    def walk(arg):
        print(arg)
        print('я иду')
    
    def add_age(self):
        self.age += 1

# person1 = Person()
# person1.add_age() # Новый вариант
# # Person.add_age(person1) # Старый вариант
# print(person1.age) # 19

# Person.age=17
# print(Person.age) # 17

# person2 = Person
# print(person2.age) # 17


class Person:
    # name = 'Арафат'
    # age = 18
    # arms = 2
    # legs = 2

    def __init__(self, name, age):
        """
        Функция, которая вызывается, когда мы создаем объект от класса
        self - ссылка на созданный объект
        """
        self.name = name
        self.age = age
    
    def add_age(self):
        """
        Функция, которая принимает объект и изменяет его возраст на +1
        """
        self.age += 1

    def __str__(self):
        """
        Функция, которая вызывается, когда мы оборачиваем объект в класс str или когда принтуем объект
        Функция __str__ ничего кроме self не принимает и обязательно должно возвращать строку
        """
        return f'{self.name} - {self.age}'

person1 = Person('Арафат', 18)
print(person1.age) # 18

person2 = Person('Неарафат', 23)
print(person2) # Неарафат - 23



"===================Атрибуты класса==================="
# атрибуты класса - переменные внутри класса

"===================Методы класса==================="
# методы клвсса - функции внутри класса

"===================Объекты класса==================="
# объект, экземлпяр, instance класса - объект, созданный по шаблону класса (он перенимает все атрибуты и методы у класса)

"===================Атрибуты и методы объекта==================="
# атрибуты и методы, которые есть у объекта, но возможно их нет у класса


class A:
    var1 = 'переменная класса'

    def __init__(self):
        self.var2 = 'переменная объекта'

print(dir(A))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1']


obj = A()
print(dir(obj))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1', 'var2']

print(A.var1) # 'переменная класса'
# print(A.var2) # AttributeError: type object 'A' has no attribute 'var2'

print(obj.var1) # 'переменная класса'
print(obj.var2) # 'переменная объекта'


""" Класс имеет доступ только к атрибутам класса """
""" Объект имеет доступ и к атрибутам класса, и к атрибутам самого объекта """