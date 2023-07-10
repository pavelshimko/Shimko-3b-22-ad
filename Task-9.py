class Rectangle():
    length = 10
    wideness = 5

    def area(self):
        area = self.length * self.wideness
        return area

print(Rectangle().area())