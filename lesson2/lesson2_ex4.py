my_str = input('Пожалуйста введите строку из нескольких слов: ')
my_list = my_str.split()

for i in range(len(my_list)):
    if len(my_list[i]) > 10:
        my_list[i] = my_list[i][0:10]
    print(my_list[i])

