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
Person()