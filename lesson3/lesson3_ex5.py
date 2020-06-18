def long_sum():
    my_sum = 0
    my_str = ''
    while True:
        my_str = input('введите числа через пробел: ')
        if 'q' in my_str:
            my_list = my_str.split()
            my_list.pop()
            for i, elem in enumerate(my_list):
                my_list[i] = int(elem)
            my_sum = my_sum + sum(my_list)
            print(f'Итоговая сумма равна: {my_sum}')
            break
        my_list = my_str.split()
        for i, elem in enumerate(my_list):
            my_list[i] = int(elem)
        my_sum = my_sum + sum(my_list)
        print(f'Сумма чисел равна {my_sum}, если хотите ввести еще числа, нажмите ENTER, для выхода q')


long_sum()