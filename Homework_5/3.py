# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
with open('text3.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

colleague_lst = []
average_salary = 0
for line in lines:
    colleague, salary = line.split()
    salary = float(salary)
    average_salary += salary
    if salary < 20000:
        colleague_lst.append(colleague)
print(f'Оклад меньше 20000 рублей у следующих сотрудников: {colleague_lst}.\nСредний доход: {average_salary / len(lines)}')










