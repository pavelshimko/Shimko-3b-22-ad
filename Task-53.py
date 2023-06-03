
class HomeWork():
    file = open("Elements.txt", 'r')
    arr = file.readline()

    def add_element(self, element = None):
        file = open("Elements.txt", 'a')
        if element:
            file.write(element)
        else:
            print(f"Нет элемента!")
        file.close()

    def remove_element(self,  element = None):
        if element in self.arr:
            self.arr = self.arr.replace(element, "")
        else:
            print(f"Нет элемента в списке")
        file = open("Elements.txt", 'w')
        file.write(self.arr)
        file.close()


    def put_on_screen(self):
        file = open("Elements.txt", 'r')
        print(file.read())
        file.close()

element = input()

HomeWork().add_element(element)
# HomeWork().remove_element(element)
# HomeWork().put_on_screen()