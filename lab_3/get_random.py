import random # модуль для получения случайного значения

def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randint(begin, end) # возврат генератора случайного значения

if __name__ == '__main__':

    data = gen_random(5, 1, 3) # массив из генераторов случайных значений
    
    print(list(data)) # вывод случайных значений

