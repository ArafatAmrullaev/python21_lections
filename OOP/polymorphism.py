"===================Полиморфизм==================="
# Полиморфизм - принцип ООП, в котором методы в разных классах называются одинаково. (один интерфейс - разный функционал)

class Dogs:
    def speak(self):
        print('Гав-гав')
        
class Cats:
    def speak(self):
        print('Мяу-мяу')

class Frogs:
    def speak(self):
        print('Ква-ква')

animals = [Cats(), Dogs(), Cats(), Frogs(), Frogs()]
for animal in animals:
    animal.speak()

print(dir(list))
print(dir(str))
print(dir(dict))

# __len__
"sdfghj" == 6
[1,2,3,[4,5,6]] == 4
{"a":1} == 1

# __add__
'a' + 'b' == 'ab'
[1, 2, 3] + [4, 5, 6] == [1, 2, 3, 4, 5, 6]
{'a':1} + {'b':2} == {'a':1, 'b':2}
4 + 6 == 10