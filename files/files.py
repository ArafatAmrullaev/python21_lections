# "================Работа с файлами=================="
# try:
#     # open открывает файл для чтения
#     file = open('test.txt')
#     # Метод read считывает файл полностью
#     output = file.read()
#     # readline() читает только одну строку
#     # readlines() читает все строки, возвращает список
#     print(output)
#     # seeker - курсор, считывающий файл
#     s1 = file.read()
#     s2 = file.read()
#     print('s1: ', s1)
#     print('s2: ', s1)
# except:
#     pass
# finally:
#     file.close()

# # Контекстный менеджер
# # with open('file.txt') as file:
# #     output = file.read()
# # print('output: ', output)

# # Типы открытия файлов
# # r (read) - стандартный тип открытия, только для чтения. Если файла нет, вызывает ошибку
# # w (write) - тип открытия только для записи. Если файла нет, создает его
# with open('write_file.txt', 'w') as file:
#     # write() записывает строку в файл
#     file.write('Hello everyone')
#     # writelines() записывает элементы итерируемого объекта в файл. Не добавляет \n автоматически
#     file.writelines(['Hello', 'World'])
#     # Если нужно, чтобы каждая строка начиналась с новой строки
#     file.write('\n'.join(['Hello', 'World']))

# # a (append) - добавляет новые записи в конец файла
# with open('write_file.txt', 'a') as file:
#     file.write('Hello world')

# # w+ - открывает файл как для чтения, так и для записи
# # r+ - открывает файл. Если не существует файла, вызывает ошибку
# # a+ - открывает файл для записи в конец. При отсутствии файла создает его
# with open('non-exist-file', 'w+'):
#     pass


"================Пакеты и модули=================="
# import file_package
# file_package.sum_file

# Один файл (file_package.py) это пакет
from file_package import read_sum_file, sum_file
sum_file(5, 5, 'arafat.txt')

a = 10
b = read_sum_file()
print(a + b)

# Папка с пакетами - модуль
