# Задание 4 (два способа, 1-й - если известно количество цифр в числе)

number = input('Введите целое двузначное число: ')
num_1 = int(number[0])
num_2 = int(number[1])

if num_1 > num_2:
    print(f'Самая большая цифра в числе: {num_1}')
else:
    print(f'Самая большая цифра в числе: {num_2}')


number = input('Введите  целое число: ')
i = 0
for num in number:
    if int(num) > i:
        i = int(num)
print(f'Самая большая цифра в числе: {i}')