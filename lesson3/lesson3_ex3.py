def my_func(a,b,c):
        my_list = [a, b, c]
        max_number = max(my_list)
        my_list.remove(max_number)
        return max_number + max(my_list)


result = my_func(-1, 11, 11)
print(result)