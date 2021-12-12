def field(items, *args):
    assert len(args) > 0 # агрументов (ключей) должно быть больше нуля
    if len(args) == 1: # если введён один аргумент (ключ)
        for d in items: # перебор предметов
            note = d.get(args[0]) # получение значения по ключу
            if note is not None: # если значение существует
                yield note # возврат генератора
    else:
        for d in items:  # перебор предметов
            dictionary = dict() # определение словаря
            for key in args: # перебор ключей
                note = d.get(key)  # получение значения по ключу
                if note is not None:  # если значение существует
                    dictionary[key] = note # запоминание значения в словарь
            if len(dictionary) != 0: # если длина полученного словаря не равна нулю
                yield dictionary # возврат генератора


if __name__ == '__main__':
    
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
        {'title': 'Шкаф', 'price': None, 'color': 'brown'},
        {'title': 'Кресло', 'price': 8000, 'color': None},
        {'title': None, 'price': 404, 'color': 'white'}
    ]
    
    arr1 = list()
    arr2 = list()

    for i in field(goods, 'title'): # вывод названий
        arr1.append(i)
    print(arr1)

    for i in field(goods, 'title', 'price', 'color'): # вывод всей информации
        arr2.append(i)
    print(arr2)
