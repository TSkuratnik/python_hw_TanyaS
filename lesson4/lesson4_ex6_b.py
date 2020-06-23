from itertools import cycle
import time


my_list = [7, 77, 777, 7777, 77777]
for number in cycle(my_list):
    print(number)
    time.sleep(1)

