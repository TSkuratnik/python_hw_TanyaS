from itertools import cycle
from time import sleep


class TrafficLight:

    def __init__(self):
        self.time_sleep = [7, 3, 4]
        self.__color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):

        for i, col in cycle(enumerate(self.__color)):
            print(col)
            sleep(self.time_sleep[i])


a = TrafficLight()
a.running()