import random

class Game_character():
    level = random.randint(1,5)
    health = random.randint(1,20) * (level /10 + 1)
    defence = random.randint(1,5)
    attack = random.randint(1,10) * (level /10 + 1)
    exp = 0

    def level_up(self, exp):
        levels_gained = int(exp / 10)
        self.level += levels_gained
        self.exp = self.exp - int(exp / 10) * 10

    def damage_hit(self, damage):
        self.health =self.health - damage + self.defence
        if self.health < 0:
            self.health = 0

def set_attrs(char1):
    char1.level = random.randint(1, 5)
    char1.health = random.randint(1, 20) * (char1.level / 10 + 1)
    char1.defence = random.randint(1, 5)
    char1.attack = random.randint(1, 10) * (char1.level / 10 + 1)
    char1.exp = 0
    return char1


def fight():
    char1 = Game_character()
    char1.name =  input('Введите имя персонажа 1 ')
    char2 = Game_character()
    char2.name = input('Введите имя персонажа 2 ')
    char1 = set_attrs(char1)
    char2 = set_attrs(char2)
    rounds = 3
    first_defeat = False
    second_defeat = False
    for i in range(rounds):
        char1.damage_hit(char2.attack), char2.damage_hit(char1.attack)
        if char1.health == 0:
            first_defeat = True
            char2.level_up(20)
            print(f'{char2.name} победил в {i + 1} раунде')
            break
        elif char2.health == 0:
            second_defeat = True
            char1.level_up(20)
            print(f'{char2.name} победил в {i + 1} раунде')
            break
        else:
            char1.level_up(10)
            char2.level_up(10)
    if not first_defeat and not second_defeat:
        if char1.health > char2.health:
            print(f"{char1.name} победил по итогу {rounds} раундов")
            char1.level_up(20)
        elif char1.health < char2.health:
            print(f"{char2.name} победил по итогу {rounds} раундов")
            char2.level_up(20)
        elif char1.health == char2.health:
            print("Победила дружба")
            char1.level_up(10)
            char2.level_up(10)

fight()