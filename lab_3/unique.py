from get_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.used_elements = set() # множество для сохранения использованных элементов
        self.data = items # изначальный массив данных
        self.ignore_case = False # значение ignore_case (по умолчанию False)
        if len(kwargs) > 0:
            self.ignore_case = kwargs['ignore_case'] # изменение значения ignore_case

    def __next__(self):
        it = iter(self.data) # итератор массива данных
        while True:
            try:
                current = next(it) # получение следующего значения
            except StopIteration: # завершение цикла при возникновении исключения
                raise StopIteration
            else:
                if self.ignore_case is True and isinstance(current, str): # проверка на ignore_case
                    current = current.lower() 
                if current not in self.used_elements: # проверка на наличие элемента во множестве элементов
                    self.used_elements.add(current) # добавление элемента во множество
                    return current # возврат текущего элемента

    def __iter__(self):
        return self

if __name__ == '__main__':
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    data2 = gen_random(10, 1, 3)
    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

    print(list(Unique(data1)))
    print(list(Unique(data2)))
    print(list(Unique(data3)))
    print(list(Unique(data3, ignore_case=True)))
