class Cell:
    def __init__(self, n):
        self.number_of_cells = n
        self.new_cell = None
        self.new_cell_sub = None
        self.new_cell_mul = None
        self.new_cell_truediv = None

    def __add__(self, other):
        self.new_cell = self.number_of_cells + other.number_of_cells
        return self

    def __sub__(self, other):
        self.new_cell_sub = self.number_of_cells - other.number_of_cells
        return self

    def newcell_sub(self):
        if self.new_cell_sub < 0:
            print('вычитание клеток невозможно')
        else:
            return self.new_cell_sub

    def __mul__(self, other):
        self.new_cell_mul = self.number_of_cells * other.number_of_cells
        return self

    def __truediv__(self, other):
        self.new_cell_truediv = self.number_of_cells // other.number_of_cells
        return self


m = Cell(10)
k = Cell(15)

m + k
print(m.new_cell)
m - k
print(m.newcell_sub())
m * k
print(m.new_cell_mul)
m / k
print(m.new_cell_truediv)


