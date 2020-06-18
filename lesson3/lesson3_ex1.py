def divide(a, b):
    while True:
        aa, bb = int(input(f'на какое число разделить {a}: ')), int(input(f'на какое число разделить {b}: '))
        try:
            return a / aa, b / bb
            break
        except ZeroDivisionError:
            print('Деление на ноль, введите другое число')


a, b = divide(10, 20)
print(a, b)