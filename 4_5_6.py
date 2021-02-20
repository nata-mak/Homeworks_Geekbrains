# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники
# на склад и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

from abc import ABC, abstractmethod


class StoreHouse:
    def __init__(self):
        self._dict = {}

    def add_to_store(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

class Equipment:
    def __init__(self, name, year, count):
        self.name = name
        self.year = year
        self.count = count
        self.group = self.__class__.__name__

    @abstractmethod
    def Action(self):
        pass

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.year} {self.count} шт'


class Printer(Equipment):
    def __init__(self, name, series, year, count):
        super().__init__(name, year, count)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.year} {self.count} шт'

    def Action(self):
        return 'Печатает'


class Scaner(Equipment):
    def __init__(self, name, series, year, count):
        super().__init__(name, year, count)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.year} {self.count} шт'

    def Action(self):
        return 'Сканирует'


class Xerox(Equipment):
    def __init__(self, name, year, count):
        super().__init__(name, year, count)

    def __repr__(self):
        return f'{self.name} {self.series} {self.year} {self.count} шт'

    def Action(self):
        return 'Копирует'


sklad = StoreHouse()
scaner = Scaner('hp', 'n656', '2019', 6)
sklad.add_to_store(scaner)
scaner = Scaner('hp', 'e440', '2020', 8)
sklad.add_to_store(scaner)
scaner = Scaner('hp', 'sc49', '2018', 3)
sklad.add_to_store(scaner)
printer = Printer('sony', 'e320', 2018, 1)
sklad.add_to_store(printer)
print(sklad._dict)
