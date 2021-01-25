# Задание 2:
time = int(input("Введите время в секундах: "))
hours = time // 3600
min = (time - hours * 3600) // 60
sec = (time - hours * 3600) - min * 60
print (f"Время в формате чч:мм:сс   {hours}:{min}:{sec}")