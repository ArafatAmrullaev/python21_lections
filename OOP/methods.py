"==================Class, static, instance methods===================="
# instance метод (метод обьекта) - метод, который принимает первым аргументом self (обьект). Вызываем instance методы у обьекта

class A:
    def instance_method(self):
        print("метод обьекта")

obj_a = A()
obj_a.instance_method() # вызываем у обьекта, и он автоматически попадает как аргумент в метод
A.instance_method(obj_a) # вызываем у класса, нужно передать обьект


# class methods (методы класса) - метод, который принимает первым аргументом cls (класс). чтобы создать метод класса, нужно метод задекорировать classmethod.

class A:
    @classmethod
    def class_method(cls):
        print(cls)
        print("Метод класса")

A.class_method()
A().class_method()


class Pizza:
    def __init__(self, radius, *ingredients):
        self.ingredients = ingredients
        self.r = radius

    def cook(self):
        print(f'Пицца размером {self.r} см\nИнгредиенты: \n{self.ingredients}')

    @classmethod
    def pepperoni(cls, r):
        return cls(r, 'пепперони', 'сыр')

    @classmethod
    def for_cheese(cls, r):
        return cls(r, 'Моцарелла','Дор блю', 'Чеддер', 'Еще сыр')


pizza1 = Pizza(30, 'сыр', 'помидоры', 'грибы')
# pizza2 = Pizza(35, 'пепперони', 'Сыр')
# pizza3 = Pizza(35, 'пепперони', 'Сыр')
pizza2 = Pizza.pepperoni(30)
pizza3 = Pizza.pepperoni(30)
pizza4 = Pizza.for_cheese(25)
pizza5 = Pizza.for_cheese(40)
pizzas = [pizza1, pizza2, pizza3, pizza4, pizza5]
for pizza in pizzas:
    pizza.cook()



# static методы - просто функции внутри класса, которые не взаимодействуют ни с классом, ни с объектом
class Square:
    def __init__(self, a):
        self.a = a
        self.s = self.get_s(a)
    
    @staticmethod
    def get_s(a):
        return a**2

sq1 = Square(4)
print(sq1.s)