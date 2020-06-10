max_number = 0
user_number = int(input('Введите целое положительное число: '))

while user_number != 0:
    numberX = user_number % 10
    print(numberX)
    user_number = user_number // 10
    if max_number < numberX:
        max_number = numberX

print('Максимальное число: ', max_number)