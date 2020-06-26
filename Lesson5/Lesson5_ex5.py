with open('ex5_file.txt', 'w+') as f:
    f.writelines(input('введите числа через пробел: '))
    f.writelines('\n')
    f.seek(0)
    numbers = f.readlines()
    list_of_numbers = numbers[0].split()
    for i, number in enumerate(list_of_numbers):
        list_of_numbers[i] = int(number)

    print(f'сумма чисел равна: {sum(list_of_numbers)}')
    f.writelines(f'Cумма чисел равна: {sum(list_of_numbers)}')

#with open('ex5_file.txt', 'a') as f:

