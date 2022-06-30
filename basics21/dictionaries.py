"================Словари=================="
# Словарь(dict) - изменяемый, итерируемый, неиндексируемый, неупорядоченный тип данных, в котором значения хранятся в парах(ключ - значение)


dict_ = {"a":'Hello', "b":2, "c":3}
print(dict_("a")) # Hello


# Ключами в словаре могут являться все неизменяемые типы данных
# Значениями в словаре могут являться любые типы данных
# Ключи должны быть уникальными

dict_ = {1:'hello',
 'a':4, 
 4.5: {'a':5},
 #{'s':5} # TypeError
 } 


"================Создание словарей=================="
dict1 = {'a':3}
dict2 = dict( [ ('key1', 'value1'), ('key2', 'value2') ] )
# dict2 = {'key1':'value1', 'key2':'value2'}
dict3 = dict( ( ['key1', 'value1'], ('key2', 'value2') ) )
# dict3 = {'key1':'value1', 'key2':'value2'}
dict4 = dict(['ab', 'cd', 'de'])
# dict4 = {"a":"b", 'c':'d', 'd':'e'}
key1, value1 = 'ab'
dict4[key1] = value1
key2, value2 = 'cd'
dict4[key2] = value2
key3, value3 = 'de'
dict4[key3] = value3


dict5 = dict(['abc']) # ValueError: dictionary update sequence element #0 has length 3; 2 is required
key1, value1 = 'abc' #
dict5[key1] = value1

"================Методы словаря=================="
 
dict_.clear() # Чистит словарь
print(dict_) # ()

dict_ = dict_.fromkeys([1, 2, 3])
print(dict_) # (1:None, 2:None, 3;None)

dict_ = dict_.fromkeys([1, 2, 3], 'hello')
print(dict_) # (1:hello, 2:hello, 3:hello)

dict_ = {"a":1, "a":2, "a":3}
print(dict_) # {"a":3}
dict_ = {"a":5}
print(dict_) # {"a":5}

dict_ = {"a":1, "b":2}
dict_["a"] # 1
dict_["c"] # KeyError

# Метод get нужен только для получения значений по ключу

dict_.get("a") # 1
dict_.get("c") # None
dict_.get("c", 5) # 5
dict_.get("a", 5) # 1

dict_.keys() # dict_keys(['a', 'b'])
dict_.values() # dict_values([1, 2])
dict_.items() # dict_items([('a', 1), ('b', 2)])

dict1 = {1:"a", 2:"b", 3:"c"}
dict2 = {3:"d", 4:"e"}
# Метод update добавляет пары из второго словаря в первый
dict1.update(dict2)
print(dict1) # {1:"a", 2:"b", 3:"d", 4:"e"}
print(dict2) # {3:"d", 4:"e"}

# Метод pop удаляет пару по ключу и возвращает значение
print(dict1.pop(3)) # d
print(dict1) # {1:"a", 2:"b", 4:"e"}
popped = dict1.pop(3)
print(popped) # d

# Метод popitem удаляет и возвращает последнуюю пару
print(dict1.popitem()) # {4, "e"}

