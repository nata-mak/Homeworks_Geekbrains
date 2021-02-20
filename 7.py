# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'z = {self.x} + {self.y}*i'

    def __add__(self, other):
        print('Сумма двух комплексных чисел равна:')
        return ComplexNumber(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        print('Произведение двух комплексных чисел равно:')
        return ComplexNumber(self.x * other.x, self.y * other.y)


number_1 = ComplexNumber(3, 4)
print(number_1)
number_2 = ComplexNumber(5, 6)
print(number_2)
res = number_1 + number_2
print(res)
mul_num = number_1 * number_2
print(mul_num)
