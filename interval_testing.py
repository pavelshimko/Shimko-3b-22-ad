class Finding_String():
    """
    Написать программу, которая принимает на вход строку и выводит на экран количество различных подстрок строки,
    начинающихся и заканчивающихся одним и тем же символом.
    """


    word = input('Введите строку ')

    """
    Собираем все буквы в строке в множество
    """
    def get_all_letters(self):
        word_letters = [x for x in self.word if x != '']
        word_letters = set(word_letters)
        return word_letters

    """
    Проходим по буквам, разделяем строку на подстроки с помощью split(), набираем их в список substring и 
    в конце считаем ее длину
    """

    def finding_substrings(self, word_letters):
        substring = []
        for i in word_letters:
            r = set(self.word.split(i)[1:-1])
            r = [f"{i+ x + i}" for x in r]
            substring.extend(r)
        number_of_substrings = len(set(substring))
        print(f'Внутри строки {self.word} есть {number_of_substrings} подстрок')
        return number_of_substrings

word_letters = Finding_String().get_all_letters()
Finding_String().finding_substrings(word_letters)
