# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("text.txt", "w") as f:
    while True:
        content = input('Введите данные: ')
        f.writelines([content, '\n'])
        if not content:
            break