import json
import sys
from print_result import print_result
from cm_timer import cm_timer_1
from unique import Unique
from field import field
from get_random import gen_random

# Сделаем другие необходимые импорты

path = r'/Users/viktorandreev/Desktop/Programming/BKIT/lab3_code/data_light.json'

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path, encoding='utf-8') as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg): # функция для возврата массива, отсортированного по названию работы
    return sorted(list(Unique(field(arg, "job-name"), ignore_case=True)), key=str.lower)


@print_result
def f2(arg): # функция для возврата массива с работами, начинающихся с "программист"
    return list(filter(lambda string: str.startswith(str.lower(string), "программист"), arg))


@print_result
def f3(arg): # функция для модификации элементов массива
    return list(map(lambda s: s + " с опытом Python", arg))


@print_result
def f4(arg): # функция для добавления зарплаты
    return dict(zip(arg, list("зарплата {} руб.".format(val) for val in gen_random(len(arg), 100000, 200000))))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
