# Задание 6:
a = int(input('Сколько км пробежал спортсмен в 1-й день? '))
b = int(input('Какой минимальный результат по количеству км должен достигнуть спортсмен? '))
i = 1

while a < b:
    print(f'{i} день: {a:.2f}')
    a = a + (a * 0.1)
    i += 1

print(f'{i} день: {a:.2f}')
print(f'На {i} день спортсмен достиг результата не менее {b} км')