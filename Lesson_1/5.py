# Задание 5:
earning = int(input('Введите вашу выручку: '))
expense = int(input('Введите ваши издержки: '))

if earning > expense:
    print('Вы отработали с прибылью.')
    rent = (earning - expense) / earning
    print('Рентабельность выручки:', rent)
else:
    print('Вы работаете с убытком.')

number = int(input('Сколько у вас на фирме сотрудников? '))
profit = (earning - expense) / number
print(f'Прибыль фирмы в расчете на одного сотрудника: {profit:.2f}')
