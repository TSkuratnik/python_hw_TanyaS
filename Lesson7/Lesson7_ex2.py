from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def fabric_consumption(self, vh):
        pass


class Coat(Cloth):
    def __init__(self, v):
        self._v = v

    @property
    def fabric_consumption(self):
        return self._v/6.5 + 0.5


class Suit(Cloth):
    def __init__(self, h):
        self._h = h

    @property
    def fabric_consumption(self):
        return 2 * self._h + 0.3


m = Coat(50)
print(m.fabric_consumption)

