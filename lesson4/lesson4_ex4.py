my_list = [1, 3, 3, 44, 5, 2, 2, 11, 11, 6]

new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)