# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    if a>b and b>c:
        return (a + b)
    elif a<b and a<c:
        return (b + c)
    else:
        return (a + c)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

result = my_func(a, b, c)
print(result)