class Book():
    name = 'Война и Мир'
    author = 'Лев Толстой'
    year_published = 1867
    genre = 'эпопея'

    def give_me_your_name(self):
        print(f"{self.name}, {self.author} ({self.year_published}), жанр {self.genre}")

Book().give_me_your_name()