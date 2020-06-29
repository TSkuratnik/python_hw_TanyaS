class Worker:
    def __init__(self):
        self.name = 'Alex'
        self.surname = 'Big'
        self.position = 'manager'
        self.__income = {'wage': 700, 'bonus': 500}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        total_income = self._Worker__income['wage'] + self._Worker__income['bonus']
        print(total_income)
        return total_income


a = Position()
a.get_full_name()
a.get_total_income()
print(a.surname)
print(a.position)

