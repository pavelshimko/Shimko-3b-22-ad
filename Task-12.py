class Student():
    name = 'Ivan'
    surname = 'Ivanov'
    year = 'first'
    accounting = 4
    cs = 5
    math = 3

    def calulate_average(self):
        aver = (self.cs + self.accounting + self.math) / 3
        return aver

print(Student().calulate_average())