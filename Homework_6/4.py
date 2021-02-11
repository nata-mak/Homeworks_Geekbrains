# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police= False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала!')
    def stop(self):
        print(f'Машина {self.name} остановилась.')
    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч')

class TownCar(Car):
    Car.is_police = False
    def show_speed(self):
        if int(self.speed) > 60:
            print('Вы превысили скорость!')
        else:
            Car.show_speed(self)

class SportCar(Car):
    def Car(self):
        Car.is_police = False

class WorkCar(Car):
    Car.is_police = False
    def show_speed(self):
        if int(self.speed) > 40:
            print('Вы превысили скорость!')
        else:
            Car.show_speed(self)

class PoliceCar(Car):
    Car.is_police = True

ford = TownCar('75','blue','ford')
ford.turn('налево')
ford.stop()
ford.show_speed()
print(ford.is_police)

maz = WorkCar('45', 'black', 'MAZ')
maz.go()
maz.stop()
maz.turn('направо')
maz.show_speed()
print(maz.is_police)

police = PoliceCar('50', 'white', 'Полиция', True)
police.go()
print(police.is_police)

bmw = SportCar('150', 'red', 'bmw')
bmw.go()
bmw.show_speed()
print(bmw.is_police)

