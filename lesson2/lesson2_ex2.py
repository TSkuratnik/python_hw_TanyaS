while True:
    try:
        my_list = []
        list_len = int(input('введите кол-во элементов в списке: '))
        for a in range(list_len):
            my_list.append(input(f'введите элемент списка №{a + 1}: '))
        break
    except ValueError:
        print('надо ввести число')

print(my_list)

if list_len % 2 == 1:
    last_element = my_list.pop()

for i in range(0, len(my_list), 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

if list_len % 2 == 1:
    my_list.append(last_element)

print(my_list)


