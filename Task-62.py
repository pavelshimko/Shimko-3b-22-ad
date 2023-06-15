class Robot():
    name = 'Robot name'
    speed = float(input('Введите скорость: '))

    def movement(self):
        time = float(input('Введите время: '))
        distance = self.speed * time
        print(f"Робот {self.name} прошел {distance} за {time}")

class Crawler_Robot(Robot):
    territory = 'territory'

class Wheel_Robot(Robot):
    make = 'make'

Crawler_Robot().movement()