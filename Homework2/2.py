# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

el_count = int(input("Введите количество элементов списка: "))
lst = []
i = 0
while i < el_count:
    lst.append(input("Введите значение списка: "))
    i += 1
print(lst)

for el in range(0, len(lst)-1, 2):
        lst[el], lst[el + 1] = lst[el + 1], lst[el]
        el += 2
print(lst)