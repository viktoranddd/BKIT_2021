data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result = sorted(data, key=abs, reverse=True) # сортировка по абсолютному значению
    print(result)

    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)  # ... с ипользованием lambda-функции
    print(result_with_lambda)
