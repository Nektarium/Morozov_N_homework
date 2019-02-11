# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('городской автомобиль поехал')

    def stop(self):
        print('городской автомобиль остановился')

    def turn(self):
        direction = input('в какую сторону вы хотите повернуть городской автомобиль?')
        print('городской автомобиль повернул ' + direction)


class SportCar:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('спорткар поехал')

    def stop(self):
        print('спорткар остановился')

    def turn(self):
        direction = input('в какую сторону вы хотите повернуть спорткар?')
        print('спорткар повернул ' + direction)


class WorkCar:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('служебный автомобиль поехал')

    def stop(self):
        print('служебный автомобиль остановился')

    def turn(self):
        direction = input('в какую сторону вы хотите повернуть служебный автомобиль?')
        print('служебный автомобиль повернул ' + direction)


class PoliceCar:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('полицеский автомобиль поехал')

    def stop(self):
        print('полицейский автомобиль остановился')

    def turn(self):
        direction = input('в какую сторону вы хотите повернуть полицейский автомобиль?')
        print('полицеский автомобиль повернул ' + direction)


town_car1 = TownCar('70', "зеленый", "opel", "не полиция")
sport_car1 = SportCar('250', "красный", "ferrari", "не полиция")
work_car1 = WorkCar('80', "белый", "ford", "не полиция")
police_car_1 = PoliceCar('100', "синий", "chevrolet", "полиция")

town_car1.go()
sport_car1.turn()
work_car1.stop()
police_car_1.go()

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('автомобиль поехал')

    def stop(self):
        print('автомобиль остановился')

    def turn(self):
        direction = input('в какую сторону вы хотите повернуть автомобиль?')
        print('автомобиль повернул ' + direction)


class TownCar(Car):

    def go(self):
        print('городской автомобиль поехал')

    def stop(self):
        print('городской автомобиль остановился')

    def turn(self):
        direction = input('в какую сторону вы хотите повернуть городской автомобиль?')
        print('городской автомобиль повернул ' + direction)


class SportCar(Car):

    def go(self):
        print('спорткар поехал')

    def stop(self):
        print('спорткар остановился')

    def turn(self):
        direction = input('в какую сторону вы хотите повернуть спорткар?')
        print('спорткар повернул ' + direction)


class WorkCar(Car):

    def go(self):
        print('служебный автомобиль поехал')

    def stop(self):
        print('служебный автомобиль остановился')

    def turn(self):
        direction = input('в какую сторону вы хотите повернуть служебный автомобиль?')
        print('служебный автомобиль повернул ' + direction)


class PoliceCar(Car):

    def go(self):
        print('полицеский автомобиль поехал')

    def stop(self):
        print('полицейский автомобиль остановился')

    def turn(self):
        direction = input('в какую сторону вы хотите повернуть полицейский автомобиль?')
        print('полицеский автомобиль повернул ' + direction)


town_car1 = TownCar('70', "зеленый", "opel", "не полиция")
sport_car1 = SportCar('250', "красный", "ferrari", "не полиция")
work_car1 = WorkCar('80', "белый", "ford", "не полиция")
police_car_1 = PoliceCar('100', "синий", "chevrolet", "полиция")

town_car1.go()
sport_car1.turn()
work_car1.stop()
police_car_1.go()

