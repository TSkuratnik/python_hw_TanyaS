from itertools import count
import time


for i in count(start= int(input('введите с какого числа начнем: ')), step=1):
    print(i)
    time.sleep(0.5)


