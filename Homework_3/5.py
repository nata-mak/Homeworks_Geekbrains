# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

def my_func(lst):
    result = 0
    for el in range(len(lst)):
        result = result + int(lst[el])
    return result

print('Для выхода нажмите "q"')
res = 0
while True:
    lst = input('Введите несколько чисел через пробел: ')
    if lst == "q":
        break
    else:
        lst = list((lst).split())
        res = res + my_func(lst)
        print(f'Сумма всех введенных вами чисел равна: {res}. Можете продолжить ввод чисел. Для выхода нажмите "q"')
print(f'Программа завершена! Сумма всех введенных вами чисел равна: {res}')
