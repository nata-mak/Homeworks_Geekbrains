# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

d = {
    'One ': 'Один',
    'Two ': 'Два',
    'Three ': 'Три',
    'Four ': 'Четыре'
}
new_lst = []

with open('text4.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()

for line in lines:
    word, number = line. split('-')
    rus_word = d[word]
    s = f'{rus_word} - {number}'
    new_lst.append(s)
    print(s)

with open('new_text4.txt', 'w', encoding='UTF-8') as f:
    f.writelines(new_lst)
