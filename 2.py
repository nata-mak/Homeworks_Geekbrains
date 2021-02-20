# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivision(Exception):
    def __init__(self, num):
        self.num = num

a = int(int(input('Введите делимое число: ')))
b = int((input('Введите делитель: ')))

try:
    result = a / b
    print(result)
    if b == 0:
        raise ZeroDivisionError
except ZeroDivisionError as err:
    print(err, '\n''На ноль делить нельзя!')
