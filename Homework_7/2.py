# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def v(self):
        return self.__v
    @v.setter
    def v(self, v):
        if v < 34:
            print('Минимальный размер пальто 34!')
            self.__v = 34
        elif v > 58:
            print('Максимальный размер пальто 58!')
            self.__v = 58
        else:
            self.__v = v

    def __str__(self):
        return f'{self.v}'

    def fabric_consumption(self):
        fc = round((self.v / 6.5 + 0.5), 2)
        return f'Расход ткани на пошив пальто: {fc} м'

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    def __str__(self):
        return f'{self.h}'

    @property
    def h(self):
        return self.__h
    @h.setter
    def h(self, h):
        if h < 1.5:
            print('Минимальный рост для пошива костюма - 1.5 м!')
            self.__h = 1.5
        elif h > 2.1:
            print('Максимальный рост для пошива костюма 2.1 м!')
            self.__h = 2.1
        else:
            self.__h = h

    def fabric_consumption(self):
        sf = round((2 * self.h + 0.3), 2)
        return f'Расход ткани на пошив костюма: {sf} м'

class General_Fabric:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def fabric_consumption(self):
        fc = round((self.v / 6.5 + 0.5), 2)
        sf = round((2 * self.h + 0.3), 2)
        res = fc + sf
        return f'Общий расход ткани на пошив пальто и костюма: {res} м'

coat = Coat(42)
c = coat.fabric_consumption()
print(c)

suit = Suit(1.7)
s = suit.fabric_consumption()
print(s)

coat_suit = General_Fabric(36, 1.6)
cs = coat_suit.fabric_consumption()
print(cs)
