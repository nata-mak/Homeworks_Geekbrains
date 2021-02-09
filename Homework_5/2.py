# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('text2.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    lines = content.splitlines()
    print(f'Количество строк в тексте: {len(lines)}')
    count = 1
    for el in lines:
        words = el.split()
        print(f'Количество слов в {count} строке: {len(words)}')
        count += 1