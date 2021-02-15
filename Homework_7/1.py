# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, arr_1, arr_2):
        self.arr_1 = arr_1
        self.arr_2 = arr_2
        self.matrix = [arr_1, arr_2]

    def __str__(self):
        return f'{self.arr_1}\n{self.arr_2}'

    def __add__(self, other):
        new_arr_1 = []
        new_arr_2 = []
        for el in range(len(self.arr_1)):
            new_arr_1.append(self.arr_1[el] + other.arr_1[el])
        for el in range(len(self.arr_2)):
            new_arr_2.append(self.arr_2[el] + other.arr_2[el])
        return f'Новая матрица:\n{Matrix(new_arr_1, new_arr_2)}'


arr_1 = [1, 2, 3, 4]
arr_2 = [5, 6, 7, 8]
matrix_1 = Matrix(arr_1, arr_2)
print(matrix_1, '\n')

arr_3 = [2, 6, 7, 0]
arr_4 = [2, 4, 6, 8]
matrix_2 = Matrix(arr_3, arr_4)
print(matrix_2, '\n')

new_matrix = matrix_1 + matrix_2
print(new_matrix)
