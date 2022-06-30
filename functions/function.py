"================Функции=================="
# Функция - именнованный блок кода, который может принимать аргументы и возвращать результат
def my_sum(a, b):
    return a+b

res = my_sum(5, 4)
print(res)


"================Параметры=================="
# Параметры - локальные переменные внутри функции, значения которых мы задаём при вызове функции (переменные, которые мы указали внутри скобочек при создании функции (когда написали def)

# Сначала определяем обязательные, затем с дефолтом, потом с *, в конце с **


"================Виды параметров=================="
# 1. Обязательные
# 2. Необязательные
# 2.1 по дефолту (со значением по умолчанию) (объявляем переменную со значением через =)
# 2.2 args
# 2.3 kwargs



"================Аргументы=================="
# Аргументы - значения, которые мы передаём параметрам при вызове функции
# Сначала всегда передаются позиционные, затем именованные


"================Виды аргументов=================="
# 1. Позиционные
# 2. Именованные (ключ=значение)


def sum_or_add_10(a, b=10):
    # b - параметр с дефолтом 10
    return a + b

print(sum_or_add_10(2, 3)) # 5
print(sum_or_add_10(5)) # 15
print(sum_or_add_10(2, 9)) # 11
print(sum_or_add_10(15)) # 25


def func(*args, **kwargs):
    '''
    args - tuple, в который нам приходят все аргументты, которые были переданы через запятую (кроме обязательных)

    kwargs - dictionary, в который нам приходят все аргументы, которые были переданы в виде ключ=значение (кроме именованных)
    '''
    print(args, kwargs)

func(1, 2, 3, 4, 5, 6, 6, 7, 7, 8, {'a':5}, a=3, b=5) #( 1, 2, 3, 4, 5, 6, 6, 7, 7, 8, {'a': 5})   {'a': 3, 'b': 5}

def func2(a, b=5, *c, **d):
    print("a -", a)
    print("b -", b)
    print("c -", c)
    print("d -", d)

# func2()   - TypeError: func2() missing 1 required positional argument: 'a'

func2(10)
# a - 10
# b - 5
# c - ()
# d - {}

func2(10,20)
# a - 10
# b - 20
# c - ()
# d - {}

func2(10,20,30,40)
# a - 10
# b - 20
# c - (30, 40)
# d - {}

func2(b=20, a=10)
# a - 10
# b - 20
# c - ()
# d - {}

# func2(10,20,30,40,a=5,b=6)   # TypeError: func2() got multiple values for argument 'a'
# потому что в переменную a позиционно мы передали 10, а именованно 5

func2(10,20, 30, 40, c=5, d=6)
# a - 10
# b - 20
# c - (30, 40)
# d - {'c': 5, 'd': 6}


"================*=================="
# * - знак умножения
# * - распаковка

list_ = [1, 2, 3, 4, 5]
list2 = [*list_] # распаковывает значение в новый список
print(list_, list2) #[1, 2, 3, 4, 5] [1, 2, 3, 4, 5]

dict_ = {'a':3, 'b':6}
dict2 = [*dict_]
print(dict_, dict2) # {'a': 3, 'b': 6} ['a', 'b']

# dict_ = {'a':3, 'b':6}
# dict2 = [**dict_]
# print(dict_, dict2)







database = {'arafat':1234, 'nearafat':4321, 'arafatne':4213}
def login(**data):
    username = data.get('username')
    password = data.get('password')

    if username in database:
        if password == database[username]:
            print('Success')
        else:
            print('Incorrect password')
    else:
        print('Incorrect username')

login(username='arafat', password=4321)


def translate(string):
    eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
    ru = "йцукенгшщзхъфывапролджэячсмитьбю"
    if string[0] in eng:
        dictionary = str.maketrans(eng, ru)
    else:    
        dictionary = str.maketrans(ru, eng)
    return string.translate(dictionary)

print(translate(input('Введите слово:')))