"================Работа с файлами=================="
# open - функция, которая позволяет открыть файл


"================Режимы=================="
# r - read (только для чтения)
# w - write (только для записи (сначала все из файла удаляется, а затем записывается))
# a - append (дозапись(все новое добавляется в конец))
# x - создает файл, если он уже существуется - ошибка
# rb - чтение в бинарном виде
# wb - запись в бинарном виде
# ab - дозапись в бинарном виде

"""Когда мы не указываем режим - по умолчанию чтенме"""
# open('test.txt') FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'

"""Когда мы открываем файл в режиме w - он создает пустой файл и потом записывает туда данные"""
# open('test.txt', 'w')  - создает пустой файл

"""Когда файла нет - он создает его"""
# open('test.txt', 'a') 



"================READ=================="
file = open('test.txt') # открываем файл в режиме чтения
res = file.read() # считывает файл и возвращает строку
print(file.read(5)) # пустая строка, потому что каретка находится в самом конце файла
file.seek(0) # каретка переходите в индекс 0 (в начало файла)
print(file.read(5)) # 'Hello' (считал 5 символов)
print(file.read(5)) # ' worl' (считал следующие символы)
print(file.tell()) # 10 (показывает текущее положение каретки)
res = file.readlines() # ['d\n', 'Makers Bootcamp\n', 'Line1\n', 'Line2\n', 'Line3\n']
file.seek(0)
file.readlines() # ['Hello World\n', 'Makers Bootcamp\n', 'Line1\n', 'Line2\n', 'Line3\n']
print(file.tell()) # 46
file.close()


"================WRITE=================="
file = open('test.txt', 'w') # открыл файл, почистил
# res = file.read()   io.UnsupportedOperation: not readable
# метод read нельзя использовать при режиме записи и дозаписи
file.write('Hello World\n') # в файл записали строку Hello World
file.write('Makers Bootcamp\n') # после этого продолжает писать строку Makers Bootcamp
file.writelines(["Line1\n", 'Line2\n', "Line3\n"]) # принимает список со строками и дозаписывает их в файл
file.close() # обязательно закрываем файл



"================With=================="
# with - конструкция, которая в начале конструкции вызывает метод __enter__, а в конце вызывает __exit__

class Test:
    def __enter__(self):
        print('Начало работы')
        return self
    
    def __exit__(self, *args, **kwargs):
        print('Конец работы')

    def hello(self):
        print('hello world')

with Test() as test:
    test.hello()
# Начало работы
# hello world
# Конец работы


file1 = open('test.txt', 'w')
file1.write('hello')
file1.close()
file2 = open('test.txt', 'w')
file2.write('world')
# file1.write('rgdsewfdd') # ValueError: I/O operation on closed file.
# потому что мы закрыли file1
file2.close()


file = open('test.txt', 'w')
file.write('Hello World\nMakers\nBootcamp')
file.seek(0)
file.write('New Lines')
file.close()


with open('test.txt') as file:
    print(file.read())
    print(file.closed) # False (closed проверяет закрыт ли файл или нет)
print(file.closed) # True