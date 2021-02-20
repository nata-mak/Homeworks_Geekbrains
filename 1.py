# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных

class Date:
    @classmethod
    def my_method(cls):
        date = input('Введите дату формата «день-месяц-год»: ')
        d, m, y = date.split('-')
        d = int(d)
        m = int(m)
        y = int(y)
        return d, m, y

    @staticmethod
    def valid_method():
        d, m, y = Date.my_method()
        res_list = []

        if d >= 1 and d <= 31:
            res_list.append(d)
        else:
            print(f'Такого числа {d} не существует!')
            return

        if m >= 1 and m <=12:
            res_list.append(m)
        else:
            print(f'Месяца {m} не существует!')
            return

        if y > 0 and y <= 2021:
            res_list.append(y)
        else:
            print('Такого года не существует!')
            return

        print(f'Дата: {res_list[0]} {res_list[1]} {res_list[2]}')

print(Date.my_method())
Date.valid_method()




