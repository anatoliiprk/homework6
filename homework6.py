#Работа со словарями
print('')
my_dict = {'Anatolii': 1995, 'Natali': 1998, 'Anastasia': 1997}
print('Мой словарь:', my_dict)
print('Анатолий:', my_dict.get('Anatolii'))
print('Егор:', my_dict.get('Egor', 'Не найдено'))
my_dict.update({'Sergey': 2000,
                'Anna': 1994})
a = my_dict.pop('Anastasia')
print('Значение удаленного ключа:', a)
print('Обновленный словарь:', my_dict)
print('')

#Работа с множествами
my_set = {1, 1, 1, 2, 3, 4, False, 0, 'Anatolii', (5, 6, 7)}
print('Моё множество:', my_set)
my_set.add('Natali')
my_set.add(79)
my_set.discard(4)
print('Измененное множество:', my_set)
