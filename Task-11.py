class Dog():
    name = 'Sharik'
    age = 3
    breed = 'husky'

    def show_data(self):
        print(f'Имя: {self.name}, порода: {self.breed},  возраст: {self.age}')

Dog().show_data()