def int_func(text):
    result = text.capitalize()
    return result


my_str = input('введите текст через пробелы, все слова с маленькой буквы: ')
my_list = my_str.split()
for i, elem in enumerate(my_list):
    my_list[i] = int_func(elem)

result_string = ' '.join(my_list)
print(result_string)