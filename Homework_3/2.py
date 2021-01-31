# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(name, surname, age, city, email, phone):
    return f'Имя: {name}, фамилия: {surname}, год рождения: {age}, город проживания: {city}, email: {email}, телефон: {phone}'

name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
age = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите ваш email: ')
phone = input('Введите ваш номер телефона: ')
print(user_data(name=name, surname=surname, age=age, city=city, email=email, phone=phone))