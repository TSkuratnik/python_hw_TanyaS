class Road:
    def __init__(self):
        self.weight_of_1_m = 25
        self.hight = 5


    def mass(self, _length, _width):
        weight_of_asphalt = _length * _width * self.weight_of_1_m * self.hight
        print(weight_of_asphalt / 1000, 'т')
        return weight_of_asphalt


a = Road()
a.mass(20, 5000)