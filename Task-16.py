class Cat():
    name = 'Барсик'
    age = 4
    colour = 'табби'

    def give_me_your_name(self):
        print(f"Кошка по имени {self.name}, Возраст {self.age}, цвет {self.colour}")

Cat().give_me_your_name()