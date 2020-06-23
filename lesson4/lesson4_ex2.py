

my_list = [50, 11, 22, 1, 13, 14, 8, 2]

new_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el - 1]]
print(new_list)