class Car:
    def __init__(self, name, color, speed):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('машина тронулась')

    def stop(self):
        print('машина остановилась')

    def turn(self, direction):
        print(f'машина повернула на{direction}')

    def show_speed(self):
        print(f'Ваша скорость {self.speed}')


class TownCar(Car):
    is_police = False

    def show_speed(self):
        print(f'Ваша скорость {self.speed}')
        if self.speed > 60:
            print('Внимание, Вы превысили скорость!')


class WorkCar(Car):
    is_police = False

    def show_speed(self):
        print(f'Ваша скорость {self.speed}')
        if self.speed > 40:
            print('Внимание, Вы превысили скорость!')


class SportCar(Car):
    is_police = False


class PoliceCar(Car):
    is_police = True


a = WorkCar('BMW', 'Red', 80)
a.show_speed()
print(a.is_police)

b = PoliceCar('BMW', 'Red', 80)
print(b.is_police)