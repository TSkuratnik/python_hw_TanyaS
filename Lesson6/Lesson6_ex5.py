class Stationery:
    def __init__(self, title):
        self.name = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой.')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом.')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером.')


a = Handle('Маркер')
a.draw()

b = Pencil('Карандаш')
b.draw()

c = Pen('Ручка')
c.draw()
print(c.name)
print(b.name)
print(a.name)
