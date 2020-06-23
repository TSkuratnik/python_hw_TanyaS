from functools import reduce
import time


def my_func(num1, num2):
    return num1 * num2


a = time.time()
my_list = [el for el in range(100, 1000) if el % 2 == 0]
print(my_list)
print(reduce(my_func, my_list))
b = time.time()
print(b - a)