"===================Абстракция==================="
# абстракция - принцип ООП, в котором создается абстрактный класс (кьасс - пустышка), в котором задаются названия аттрибутов и методов для того, чтобы в дочерних классах переопределить их нужным образом. От абстрактных классов мы не создаем объектов, потому что в них есть только названия и нет логики

from abc import ABC, abstractclassmethod, abstractproperty
class AbstractAnimal(ABC):
    @abstractclassmethod
    def voice(self):
        ...
    
    @abstractproperty
    def legs(self):
        ...

# obj = AbstractAnimal() # TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods legs, voice

class Dog(AbstractAnimal): ...

# obj = Dog() # TypeError: Can't instantiate abstract class Dog with abstract methods legs, voice

class Dog(AbstractAnimal):
    def voice(self):
        print('гав-гав')

# obj = Dog() # TypeError: Can't instantiate abstract class Dog with abstract methods legs

class Dog(AbstractAnimal):
    legs = 4
    def voice(self):
        print('гав-гав')

class Cat(AbstractAnimal):
    legs = 4
    def voice(self):
        print('мяу-мяу')


obj = Dog()
obj.voice() # гав-гав

obj1 = Cat()
print(obj1.legs) # 4

