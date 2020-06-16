my_list = [7, 5, 3, 3, 2]
new_element = int(input('введите число: '))
if new_element <= my_list[-1]:
    my_list.append(new_element)
else:
    for i in range(len(my_list)):
        if new_element > my_list[i]:
            my_list.insert(i, new_element)
            break

print(my_list)