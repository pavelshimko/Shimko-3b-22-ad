class Car():
    make = 'BMW'
    model = 'Series 3'
    year = 1975
    price = 100000

    def give_me_your_name(self):
        print(f"{self.make}-{self.model}, {self.year}, {self.price}")

Car().give_me_your_name()