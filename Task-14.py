class Student():
    name = 'Ivan'
    surname = 'Ivanov'
    age = 22
    speciality = 'cs'

    def give_me_your_name(self):
        print(f"{self.name}-{self.surname}, {self.age}, {self.speciality}")

Student().give_me_your_name()