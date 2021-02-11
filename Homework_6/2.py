# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def weight(self, length, width):
        self._length = length
        self._width = width
        weight = length * width * 25 * 0.05  # 5 см перевела в м, так как предполагаю, что длину и ширину задаем в м
        print(f'Необходимая масса асфальта: {weight} кг')

road_1 = Road()
road_1.weight(20, 5000)
