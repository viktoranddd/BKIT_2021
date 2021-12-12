def print_result(func_to_decorate):
    def decorated_func(*args, **kwargs):
        incoming = func_to_decorate(*args, **kwargs) # получение значения функции
        print(func_to_decorate.__name__) # вывод названия функции
        if isinstance(incoming, list): # если значение - список
            for i in incoming:
                print(i)
        elif isinstance(incoming, dict):  # если значение - словарь
            for i in incoming:
                print(str(i) + " = " + str(incoming[i]))
        else: # иное значение
            print(incoming)
        return incoming

    return decorated_func


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
