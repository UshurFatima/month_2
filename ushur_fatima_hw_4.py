from random import randint, choice


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f"{self.__name} health: {self.__health} damage: {self.__damage}"


# global variable
round_number = 0


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def hit(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if type(hero) == Berserk and self.defence != "BLOCK_DAMAGE_AND_REVERT":
                    blocked = randint(1, 2) * 5
                    hero.blocked_damage = blocked
                    hero.health -= (self.damage - blocked)
                else:
                    hero.health -= self.damage

    def choose_defence(self, heroes):
        random_hero: Hero = choice(heroes)
        self.__defence = random_hero.ability

    def __str__(self):
        return "BOSS " + super().__str__() + f" defence: {self.__defence}"


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def hit(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "CRITICAL_DAMAGE")

    # реализация способности воина - CRITICAL DAMAGE
    def apply_super_power(self, boss, heroes):
        random_coefficient = randint(2, 4)
        boss.health -= self.damage * random_coefficient
        print(f"Warrior {self.name} hit critically {self.damage * random_coefficient}.")


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "BOOST")

    # реализация способности мага - BOOST
    def apply_super_power(self, boss, heroes):
        boost_points = randint(1, 4) * 2
        for hero in heroes:
            if self != hero:
                hero.damage += boost_points
        print(f"Magic {self.name} boosted {boost_points} to heroes")


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "BLOCK_DAMAGE_AND_REVERT")
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    # реализация способности берсерка - BLOCK_DAMAGE_AND_REVERT
    def apply_super_power(self, boss, heroes):
        boss.health -= self.blocked_damage
        print(f"Berserk {self.name} reverted {self.__blocked_damage} to boss.")


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, "HEAL")
        self.__heal_points = heal_points

    @property
    def heal_points(self):
        return self.__heal_points

    # реализация способности медика - HEAL
    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "ADD_HEALTH")

    # реализация способности хакера - ADD_HEALTH
    def apply_super_power(self, boss, heroes):
        if round_number % 2 != 0:
            taken_health = randint(1, 2) * 5
            boss.health -= taken_health
            chosen_hero = choice(heroes)
            if chosen_hero != self:
                chosen_hero.health += taken_health
                print(f"Hero {chosen_hero.name} was given {taken_health} health_points")


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "REVIVE")

    # реализация способности Witcher - REVIVE
    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health == 0:
                hero.health += self.health
                self.health = 0
                print(f"Hero {hero.name} was revived")
                break


class Ludoman(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "DICE")

    # реализация способности лудомана - DICE
    def apply_super_power(self, boss, heroes):
        dice_1 = randint(1, 6)
        dice_2 = randint(1, 6)
        if dice_1 == dice_2:
            boss.health -= dice_2 * dice_1
            print(f"{dice_1 * dice_2} health points were taken from boss")
        else:
            unlucky_hero = choice(heroes)
            unlucky_hero.health -= (dice_2 + dice_1)
            print(f"{dice_1 + dice_2} health points were taken from {unlucky_hero.name}")


class Samurai(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "SHURIKEN")

    # реализация способности самурая - SHURIKEN
    def apply_super_power(self, boss, heroes):
        shurikens = ["virus", "vaccine"]
        random_shuriken = choice(shurikens)
        if random_shuriken == "virus":
            boss.health -= 10
        elif random_shuriken == "vaccine":
            boss.health += 10
        print(f"{random_shuriken} shuriken was thrown")


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print("Heroes won!!!")
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print("Boss won!!!")
        return True
    return False


def show_statistics(boss, heroes):
    print(f"ROUND - {round_number} -------------------")
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    # here only local variables, so we need to connect to global variable
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and hero.ability != boss.defence:
            hero.hit(boss)
            hero.apply_super_power(boss, heroes)

    show_statistics(boss, heroes)


def start_game():
    boss = Boss("Diablo", 2000, 50)
    warrior_1 = Warrior("Rubi", 280, 10)
    warrior_2 = Warrior("Reksar", 270, 15)
    magic = Magic("Hendolf", 290, 10)
    berserk = Berserk("Guts", 260, 5)
    doc = Medic("Jojo", 250, 5, 15)
    assistant = Medic("Lily", 300, 5, 5)
    witcher = Witcher("Albert", 300, 0)
    hacker = Hacker("Bob", 250, 10)
    ludoman = Ludoman("Zane", 230, 10)
    samurai = Samurai("Minamoto", 290, 15)

    heroes_list = [warrior_1, warrior_2, doc, magic, berserk,
                   assistant, witcher, hacker, ludoman, samurai]

    show_statistics(boss, heroes_list)

    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()
